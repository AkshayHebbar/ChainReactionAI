# Insert any rough code or module which can be used in the program


Structure:

Board.py
- Board = Returns the empty board
- valid states = Returns the empty locations + current players states
- opponent states in proximity = returns the opponent orbs nearby

populateAtom.py
- insertAtom = inserts atom at a particular location on the board and returns the board
- createChain = creates a chain reaction if present and returns the final state of the board
'''
def interact_inplace(board: list, move: int, player: int) -> bool:
    """
    Interact with Chain Reaction Environment
    Modifies board inplace
    Note: Does not check if game was over, do checking outside
    """

    # setup
    psign = -1 if player else 1
    game_over = False

    # using queue to sequentialize steps
    # near cells are calculated first
    work = queue.Queue()
    work.put(move)

    # store counts
    pos, neg = 0, 0
    for elem in board:
        pos += elem > 0
        neg += elem < 0

    # swap counts if player is 1
    t_frn, t_enm = (neg, pos) if player else (pos, neg)

    while not (work.empty() or game_over):
        # get next index in queue
        idx = work.get()

        # update territory count and game over flag
        t_frn += 1
        t_enm -= board[idx] * psign < 0
        game_over = (t_frn + t_enm > 2) and (t_enm == 0)

        # update orb count according to rule
        orbct = abs(board[idx]) + 1
        maxcp = len(NTABLE[idx])
        board[idx] = (orbct % maxcp) * psign

        # append next indices if exploded
        if orbct == maxcp:
            [work.put(i) for i in NTABLE[idx]]

    return game_over

'''


AI
- Minimax = provides the utilities after playing minimax algo
- Baseline AI = random actions
- human = call valid states and print the options

Display board
- print board
- print atoms/orbs at a particular location.

'''
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16

m = 5
n = 5

plt.figure(figsize=(n+1, m+1))
plt.text(2-0.5, 3-0.5, 'p1',horizontalalignment='center',verticalalignment='center')
plt.text(1-0.5, 5-0.5, 'o1',horizontalalignment='center',verticalalignment='center')

plt.axis([0, (n), (m ), 0])
plt.xticks(np.linspace(0, (n ), n +1), [])
plt.yticks(np.linspace(0, (m ), m +1), [])
plt.grid(linestyle="solid")
plt.savefig("Table.png", dpi=300)
plt.show()
'''
