import numpy as np
from PlayGame.play_game import insert_atom
from Util.utilities import *

def find_max_path(board, player, util):
  for i,v in enumerate(board):
    for j,t in enumerate(v):
      if np.sign(board[i,j]) != np.sign(player):
        for k,l in get_adjacent(board,(i,j)):
          if np.sign(board[k,l]) != np.sign(player) :
            util[k,l]-= board[i,j]
          else:
            util[k,l]+= board[i,j]
  return np.negative(util)

def calculate_heuristic(board,player):
  util = np.array([board[i,j] * (3/check_instability(board,(i,j))) for i,v in enumerate(board) for j,t in enumerate(v)]).reshape(board.shape)
  util = find_max_path(board,player,util)
  return util.sum()

def evaluate(board,player):
  heur_util = calculate_heuristic(board,player)
  return heur_util

def calculate_score(board):
  m,n = board.shape
  pos = [(i,j) for i,v in enumerate(board) for j,t in enumerate(v)]
  # multiply the atom count by its inverse instability 
  utilities = np.array( [board[p] * (3/check_instability(board,p)) for p in pos])
  # add all the values and round off the score to the next integer
  return int(np.ceil(utilities.sum()))

def minimax(state:tuple,max_depth,evaluate):
  board,player = state
  new_board = board.copy()

  #base cases:
  if game_over(new_board,player): return None, calculate_score(new_board) # calculate score if game over
  if max_depth == 0: return None, evaluate(new_board,player) #at max depth calculate evaluation

  children = [insert_atom(new_board.copy(),(row,col),player) for row,col in valid_states(new_board,player)]

  #print("children\n",children)
  results = [minimax((child,player), max_depth-1, evaluate) for child in children]
  _, utilities = zip(*results)
  
  if player == -1: action = np.argmax(utilities)
  if player == 1: action = np.argmin(utilities)

  return children[action], utilities[action]

def treeAI(board,player):
  board,heur = minimax((board,player),2,evaluate)
  return board,np.negative(player)
