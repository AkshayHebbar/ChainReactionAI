import numpy as np
import matplotlib.pyplot as pt
import torch as tr
from Backend.cr_minimax import minimax,evaluate
from CreateBoard.create_board import init
from Util.utilities import *
from PlayGame.play_game import insert_atom

# Code to generate training data
# Each training example is an intermediate game state, paired with its minimax value

def random_state(depth=0, size=(3,3)):
    m,n=size
    print(m,n)
    state = init(m,n)
    board,player = state
    for d in range(depth):
        actions = [(x,y) for x,y in valid_states(board,player)]
        if len(actions) == 0: break
        action = actions[np.random.randint(len(actions))]
        state = insert_atom(board,action,player)
    return state
# Used to generate a training data set
# Samples random states at a given depth and then calculates their minimax value
def generate(num_examples, depth, size):
    examples = []
    for n in range(num_examples):
        state = random_state(depth, size)
        board,player = state
        nodecount=0
        utility = minimax(state,depth,evaluate(board,player),nodecount)[2]
        examples.append((state, utility))
    return examples

# Augment data with rotations and reflections
def augment(examples):
    augmented = []
    for state, utility in examples:
        for k in range(4):
            rot = np.rot90(state[0], k)
            augmented.append((rot, utility)) # rotate board
            augmented.append((rot[:,::-1], utility)) # mirror of rotated board
    return augmented

# Used to convert a game state to a tensor encoding suitable for NN input
# Uses one-hot encoding at each grid position
def encode(state):
    # encoding[0,:,:] == 1 where there are "_"s, 0 elsewhere
    # encoding[1,:,:] == 1 where there are "O"s, 0 elsewhere
    # encoding[2,:,:] == 1 where there are "X"s, 0 elsewhere
    symbols = np.array([0,1,-1]).reshape(-1,1,1)
    onehot = (symbols == np.sign(state[0])).astype(np.float32)
    return tr.tensor(onehot)


def generate_examples():
    # Generate a lot of training/testing data
    training_examples = generate(num_examples = 100, depth=10, size=(4,4))
    testing_examples = generate(num_examples = 50, depth=10, size=(4,4))

    # augment training data
    print("Not Augmented",len(training_examples))
    training_examples = augment(training_examples)
    print("Augmented",len(training_examples))

    _, utilities = zip(*testing_examples)
    baseline_error =sum((u-0)**2 for u in utilities) / len(utilities)
    print("Baseline Error",baseline_error)
    print("training Ex:", training_examples[0])
    return training_examples,testing_examples, baseline_error
