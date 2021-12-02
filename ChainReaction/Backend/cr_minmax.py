import numpy as np


def find_max_path(board, util):
  for i,v in enumerate(board):
    for j,t in enumerate(v):
      for k,l in get_adjacent(board,(i,j)):
        if np.sign(board[k,l]) == np.sign(board[i,j]) :
          util[i,j]+= board[k,l]

          if(np.argmax(util[i]) == j or (np.argmax(util[i]) in [j for i,j in get_adjacent(board,(k,l))] ) ):
            util[i,j] += np.sqrt(np.square(k-i)+np.square(l-j))
          else:
            util[i,j] -= np.sqrt(np.square(k-i)+np.square(l-j))
  return util

def calculate_heuristic(board):
  util = np.array([board[i,j] * (3/check_instability(board,(i,j))) for i,v in enumerate(board) for j,t in enumerate(v)]).reshape(board.shape)
  util = find_max_path(board,util)
  print("util: \n",util)
  for row in util:
    print("argmax:",np.argmax(row))

  print("utility\n",np.negative(util))
  return board.sum()

def evaluate(board):
  return calculate_heuristic(board)

def calculate_max_utility(board):
  m,n = board.shape
  new_board = create_board(m,n)
  pos = [(i,j) for i,v in enumerate(new_board) for j,t in enumerate(v)]
  utilities = np.array([3/check_instability(new_board,p) for p in pos])
  return int(np.floor(utilities.sum()))

def calculate_utility(board):
  m,n = board.shape
  pos = [(i,j) for i,v in enumerate(board) for j,t in enumerate(v)]
  utilities = np.array( [board[p] * (3/check_instability(board,p)) for p in pos])
  return int(np.floor(utilities.sum()))

def minimax(board,max_depth,evaluate,player):
  new_board = board.copy()
  if game_over(new_board,player):  calculate_utility(new_board)
  if max_depth == 0: return None, evaluate(new_board)
  print([(row,col) for row,col in valid_states(new_board,player)])
  children = [insert_atom(new_board.copy(),(row,col),player) for row,col in valid_states(new_board,player)]
  print("children\n",children)
  results = [minimax(child, max_depth-1, evaluate,player) for child in children]
  print(results)
  _, utilities = zip(*results)
  print(utilities)
  action = np.argmax(utilities)
  print("action:", action)
  print("utilities[action] :",utilities[action])
  print(board)
  print("children's action \n",children[action])
  return children[action], utilities[action]
