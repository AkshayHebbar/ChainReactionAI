import numpy as np
import matplotlib.pyplot as pt
import torch as tr

# Code to generate training data
# Each training example is an intermediate game state, paired with its minimax value

# The minimax algorithm
def minimax(state):
    if state.is_leaf():
        return state.score_for_max_player()
    else:
        child_utilities = [
            minimax(state.perform(action))
            for action in state.valid_actions()]
        if state.is_max_players_turn(): return max(child_utilities)
        if state.is_min_players_turn(): return min(child_utilities)

# Used to get a random state somewhere in the game tree for a training example
# Performs random actions for the given number of turns (depth parameter)
def random_state(depth=0, size=3):
    state = initial_state(size)
    for d in range(depth):
        actions = state.valid_actions()
        if len(actions) == 0: break
        action = actions[np.random.randint(len(actions))]
        state = state.perform(action)
    return state

# Used to generate a training data set
# Samples random states at a given depth and then calculates their minimax value
def generate(num_examples, depth, size):
    examples = []
    for n in range(num_examples):
        state = random_state(depth, size)
        utility = minimax(state)
        examples.append((state, utility))
    return examples

# Augment data with rotations and reflections
def augment(examples):
    augmented = []
    for state, utility in examples:
        for k in range(4):
            rot = np.rot90(state.board, k)
            augmented.append((TicTacToeState(rot), utility))
            augmented.append((TicTacToeState(rot[:,::-1]), utility))
    return augmented

# Used to convert a game state to a tensor encoding suitable for NN input
# Uses one-hot encoding at each grid position
def encode(state):
    # encoding[0,:,:] == 1 where there are "_"s, 0 elsewhere
    # encoding[1,:,:] == 1 where there are "O"s, 0 elsewhere
    # encoding[2,:,:] == 1 where there are "X"s, 0 elsewhere
    symbols = np.array(["_","O","X"]).reshape(-1,1,1)
    onehot = (symbols == state.board).astype(np.float32)
    return tr.tensor(onehot)



#############

def dl_minimax(state, max_depth, eval_fn):
    if state.is_leaf():
        return 0, state.score_for_max_player()
    elif max_depth == 0:
        return 0, eval_fn(state)
    else:
        child_utilities = [
            dl_minimax(state.perform(action), max_depth-1, eval_fn)[1]
            for action in state.valid_actions()]

        if state.is_max_players_turn(): a = np.argmax(child_utilities)
        if state.is_min_players_turn(): a = np.argmin(child_utilities)

        return a, child_utilities[a]

# Baseline AI uses a very simple evaluation function that always returns 0 for non-leaf nodes
simple_eval = lambda state: 0

# The other AI uses the NN for its eval_fn
def nn_eval(state):
    with tr.no_grad():
        utility = net(encode(state).unsqueeze(0))

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
    return utility
