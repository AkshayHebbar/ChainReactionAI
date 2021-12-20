#Author: Akshay Hebbar

import numpy as np
from Util.utilities import *
#from Display.print_board import print_board
import time

def insert_atom(board,pos:tuple,player:int):
  #x,y = val
  #plr = 1 if player>0 else -1
  #insert_success = False
  #check if pos is valid in grid
  if(board[pos]==0):
    #board[pos]+= plr
    board[pos]+= player
    #print_board(board,player)
    player = player*-1
  elif(np.sign(board[pos]) == player):
    board = create_chain(board,pos,player)
    #print_board(board,player)
    player = player*-1
  else:
    print("**Invalid Action! Try a different square**")
  return (board,player)


def create_chain(board,pos:tuple,player:int):
  #print("creating chain\n",board, pos)

  if(abs(board[pos])<check_instability(board,pos)):
    board[pos] = player*(abs(board[pos])+1)
  else:  
    neighbors = [(x,y) for x,y in get_adjacent(board,pos)]
    board[pos] = 0
    while(neighbors):
      i = neighbors[0]
      neighbors.remove(i)
      if(abs(board[i])<(check_instability(board,i))):
        board[i] = player*(abs(board[i])+1)
      else:
        board[i]=0
        neighbors = [(x,y) for x,y in get_adjacent(board,i)] + neighbors
      #print("chain neighbors", neighbors)
      if game_over(board,player):
        neighbors.clear()
  return board       



#  if(abs(board[pos])< check_instability(board,pos)):
#    board[pos] = player*(abs(board[pos])+1)
#  else:
#    neighbors = get_adjacent(board,pos)
#    board[pos] = 0
#    for i in neighbors:
#      x,y = i
#      create_chain(board,(x,y),player)
#  # print_board(board)
#  return board
