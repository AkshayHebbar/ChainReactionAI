import numpy as np
from Util.utilities import *
from Display.print_board import print_board

def insert_atom(board,pos:tuple,player:int):
  #x,y = val
  #plr = 1 if player>0 else -1
  #insert_success = False
  #check if pos is valid in grid
  if(board[pos]==0):
    #board[pos]+= plr
    board[pos]+= player
    print_board(board,player)
    player = player*-1
  elif(np.sign(board[pos]) == player):
    board = create_chain(board,pos,player)
    print_board(board,player)
    player = player*-1
  else:
    print("**Invalid Action! Try a different square**")  
  return (board,player)


def create_chain(board,pos:tuple,player:int):
  instability = check_instability(board,pos)
  if(abs(board[pos])< instability):
    board[pos] = player*(abs(board[pos])+1)
  else:
    neighbors = get_adjacent(board,pos)
    board[pos] = 0
    for i in neighbors:
      x,y = i
      create_chain(board,(x,y),player)
  # print_board(board)
  return board
