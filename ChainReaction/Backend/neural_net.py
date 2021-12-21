import torch as tr
import numpy as np
import matplotlib.pyplot as pt
from Backend.cr_minimax import calculate_score
from Util.utilities import *
from PlayGame.play_game import insert_atom
from Backend.generate_training import generate_examples,encode

# Defines a network with two fully-connected layers and tanh activation functions
class LinNet(tr.nn.Module):
    def __init__(self, size, hid_features):
        super(LinNet, self).__init__()
        self.to_hidden = tr.nn.Linear(3*size**2, hid_features)
        self.to_output = tr.nn.Linear(hid_features, 1)
    def forward(self, x):
        h = tr.relu(self.to_hidden(x.reshape(x.shape[0],-1)))
        y = tr.tanh(self.to_output(h))
        return y

class ConvNet(tr.nn.Module):
    def __init__(self, size, hid_features):
        super(ConvNet, self).__init__()
        self.to_hidden = tr.nn.Conv2d(3, hid_features, 2)
        self.to_output = tr.nn.Linear(hid_features*(size-1)**2, 1)
    def forward(self, x):
        h = tr.relu(self.to_hidden(x))
        y = tr.tanh(self.to_output(h.reshape(x.shape[0],-1)))
        return y

def cnn_viz(net):
    numrows = net.to_hidden.weight.shape[0] # out channels
    numcols = net.to_hidden.weight.shape[1] # in channels
    pt.figure(figsize=(numcols, numrows))

    sp = 0
    for r in range(numrows):
        for c in range(numcols):
            sp += 1
            pt.subplot(numrows, numcols, sp)
            pt.imshow(net.to_hidden.weight[r,c].detach().numpy(), cmap="gray")
    pt.show(block=False)

def example_error(net, example):
    state, utility = example
    x = encode(state).unsqueeze(0)
    y = net(x)
    e = (y - utility)**2
    return e

# Calculates the error on a batch of training examples
def batch_error(net, batch):
    states, utilities = batch
    u = utilities.reshape(-1,1).float()
    print("States ",states[1])
    y = net(states)
    e = tr.sum((y - u)**2) / utilities.shape[0]
    return e

def nn_create():
    net = ConvNet(size=4, hid_features=4)
    cnn_viz(net)
    optimizer = tr.optim.SGD(net.parameters(), lr=0.00001, momentum=0.9)

    #training_examples,testing_examples,baseline = generate_examples()
    #print("train:", training_examples[1])
    
    states, utilities = zip(*training_examples)
    training_batch = tr.stack(tuple(map(encode, states))), tr.tensor(utilities)

    print("train",training_batch[1])

    states, utilities = zip(*testing_examples)
    testing_batch = tr.stack(tuple(map(encode, states))), tr.tensor(utilities)
    
    curves = [], []
    for epoch in range(50000):    
        # zero out the gradients for the next backward pass
        optimizer.zero_grad()
        e = batch_error(net, training_batch)
        e.backward()
        training_error = e.item()

        with tr.no_grad():
            e = batch_error(net, testing_batch)
            testing_error = e.item()
    optimizer.step()
    if epoch % 1000 == 0:
        print("%d: %f, %f" % (epoch, training_error, testing_error))
    curves[0].append(training_error)
    curves[1].append(testing_error)
    return net
    

def nn_eval(state):
    net = nn_create()
    with tr.no_grad():
        utility = net(encode(state).unsqueeze(0))
    return utility

def dl_minimax(state, max_depth, eval_fn):
    board,player = state
    if game_over(board,player):
        return 0, calculate_score(board,player)
    elif max_depth == 0:
        return 0, eval_fn(state)
    else:
        child_utilities = [
            dl_minimax(insert_atom(board,(row,col),player), max_depth-1, eval_fn(state))[1]
            for row,col in valid_states(board,player)]

        if player == -1: a = np.argmax(child_utilities)
        if player == 1: a = np.argmin(child_utilities)

        return a, child_utilities[a]
