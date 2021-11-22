# Insert any rough code or module which can be used in the program


Structure:

Board.py
- Board = Returns the empty board
- valid states = Returns the empty locations + current players states
- opponent states in proximity = returns the opponent orbs nearby

populateAtom.py
- insertAtom = inserts atom at a particular location on the board and returns the board
- createChain = creates a chain reaction if present and returns the final state of the board

AI
- Minimax = provides the utilities after playing minimax algo
- Baseline AI = random actions
- human = call valid states and print the options

Display board
- print board
- print atoms/orbs at a particular location.
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16

m = 5
n = 5

plt.figure(figsize=(n+1, m+1))
'''for krow, row in enumerate(A):
    plt.text(5, 10*krow + 15, Y[krow],
             horizontalalignment='center',
             verticalalignment='center')
    for kcol, num in enumerate(row):
        if krow == 0:
            plt.text(10*kcol + 15, 5, X[kcol],
                     horizontalalignment='center',
                     verticalalignment='center')
        plt.text(10*kcol + 15, 10*krow + 15, num,
                 horizontalalignment='center',
                 verticalalignment='center')
'''
plt.text(2-0.5, 3-0.5, 'p1',horizontalalignment='center',verticalalignment='center')
plt.text(1-0.5, 5-0.5, 'o1',horizontalalignment='center',verticalalignment='center')

plt.axis([0, (n), (m ), 0])
plt.xticks(np.linspace(0, (n ), n +1), [])
plt.yticks(np.linspace(0, (m ), m +1), [])
plt.grid(linestyle="solid")
plt.savefig("Table.png", dpi=300)
plt.show()
