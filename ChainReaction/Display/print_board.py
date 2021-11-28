import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from Util.utilities import valid_states

def print_board(board, player):
    rcParams['font.family'] = 'serif'
    rcParams['font.size'] = 16
    m,n = board.shape

    plr1_pos =[(x,y) for x,y in zip(*np.where(board>0))]
    #print(" player 1 : " , list(plr1_pos))

    plr2_pos =[(x,y) for x,y in zip(*np.where(board<0))]
    #print(" player 2 : " , list(plr2_pos))
    plt.figure(figsize=(m,n))
    
    plt.axis([0, (n), (m ), 0])
    plt.xticks(np.linspace(0, n, n+1 ), [])
    plt.yticks(np.linspace(0, m, m+1), [])
    plt.grid(linestyle="solid")

    for (x,y) in plr1_pos:
      plt.text(y+0.5, x+0.5, 'p'+str(board[x,y]),horizontalalignment='center',verticalalignment='center', color ='green')
    for (x,y) in plr2_pos:
      plt.text(y+0.5, x+0.5, 'o'+str(abs(board[x,y])),horizontalalignment='center',verticalalignment='center',color = 'red')
    plt.savefig("Board.png", dpi=300,format='png')
    #plt.text(m+1,n-1, 'Choose action:\n ' +str(valid_states(board,player)), verticalalignment='center', fontsize = 10)
    plt.title("Chain Reaction")
    plt.xlabel('Choose action: ' +str([(x,y) for x,y in valid_states(board,player)]), loc='left')
    plt.ion()
    plt.show(block = False)
    plt.pause(0.01)
    plt.close()
