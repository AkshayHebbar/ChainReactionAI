#Author : Akshay Hebbar
import numpy as np
import signal
from PlayGame.play_game import insert_atom
from Util.utilities import *
from copy import deepcopy

def find_max_path(board, player, util):
  
  for i,v in enumerate(board):
    for j,t in enumerate(v):
      base_val = np.zeros(util.shape)
      print("Calculating for pos:",(i,j))
      # colony density calculation: using nearest neighbor of same type
      if np.sign(board[i,j]) == np.sign(player):  # checking for same type as that of player
        neighbors = [(k,l) for k,l in get_adjacent(board,(i,j))]  # get all neighboring positions
        print("initial base val: ", base_val)
        for pos in neighbors:
          print("neighbor pos:", pos)
          if np.sign(board[i,j]) == np.sign(board[pos]):  # Check if the sign of a neighbor matches
            base_val[i,j] += util[pos] # add neighbors utility values
            pos_adj = [(x,y) for x,y in get_adjacent(board,pos)]
            neighbors = list(set().union(*[neighbors, pos_adj]))
            neighbors.remove(pos)
            print("same neighbor base val: ", base_val)
          else:
            #condition where atom at i,j is next to a pos of opposite player having high instability
            if abs(board[pos])* check_instability(board,pos)==3:
              base_val[i,j] += util[i,j]
              print("neighbor is instable:",base_val)
              #case for places next to exploding atom of opponents
            elif abs(util[i,j])>=abs(util[pos]):
              base_val[i,j] -= util[pos]
              print("neighbor and val is instable:",base_val)
            else:
              base_val[i,j] += board[pos]*(3/check_instability(board,pos))
              print("different neighbor base val: ", base_val)

        print("base_val before",base_val)
        base_val[i,j] += player*check_instability(board,(i,j)) # adding instability values        
        print("base_val after",base_val)
        print("util:",util)
        util += base_val
      else:
        continue
         
  print("final util",util)
  return util

def calculate_heuristic(board,player,optimize):
  util = np.array([board[i,j] * (3/check_instability(board,(i,j))) for i,v in enumerate(board) for j,w in enumerate(v)]).reshape(board.shape)
  nutil = calculate_score(util,-1)-calculate_score(util,1)
  if optimize:
    nutil = find_max_path(board,player,util)
  return nutil.sum()

def evaluate(board,player):
  optimize = False
  heur_util = calculate_heuristic(board,player,optimize)
  return heur_util/10

def calculate_score(board,player):
  m,n = board.shape
  #pos = [(i,j) for i,v in enumerate(board) for j,t in enumerate(v)]
  pos = [(x,y) for x,y in zip(*np.where(player*board>0))]
  # multiply the atom count by its inverse instability 
  utilities = np.array( [board[p] * (3/check_instability(board,p)) for p in pos])
  # add all the values and round off the score to the next integer
  score = utilities.sum()
  #score = board.sum()
  return score *(m+n) * player

def minimax(state:tuple,max_depth,evaluate, nodecount):
  
  board,player = state
  new_board = board.copy()

  children = [insert_atom(new_board.copy(),(row,col),player) for row,col in valid_states(new_board,player)]
  #print("Children nodes : ",len(children))
  nodecount += len(children)
  
  #base cases:
  if game_over(board,np.negative(player)): children.clear() ;return None, calculate_score(new_board,player),nodecount# calculate score if game over
  if max_depth == 0: return None, evaluate(new_board,player),nodecount #evaluate(new_board,player) #at max depth calculate evaluation
  
  results = [minimax(child, max_depth-1, evaluate,nodecount)[:2] for child in children]
  _, utilities= zip(*results)
  
  if player == -1: action = np.argmax(utilities)
  if player == 1: action = np.argmin(utilities)

  return children[action], utilities[action],nodecount

def treeAI(board,player):
  nodecount = 0
  #print("brd\n",board)
  ai_board,utility,nodes = minimax((board,player),2,evaluate,nodecount)

  updated_board = ai_board[0]
  #print(updated_board)
  pboard = [(x,y) for x,y in zip(*np.where(player*board>0))]
  pupdated = [(x,y) for x,y in zip(*np.where(player*updated_board>0))]
  new_pos =(-1,-1)
  for i in pupdated:
    if(np.abs(updated_board[i]-board[i])>0):
      new_pos = i

  return new_pos,nodes
