import numpy as np

def valid_states(board,player):
  return np.array([*zip(*np.where(board<=0))]) if player<0 else np.array([*zip(*np.where(board>=0))])

def game_over(board,player):
  m,n = board.shape
  return np.all(board *player >=0)and abs(board.sum()) > (2 if m*n>1 else 0)

def get_adjacent(board,pos:tuple):
  x,y = pos
  m,n = board.shape

  if pos>(m-1,n-1) or pos < (0,0):
    print("position outside board")
    return []

  x_left = x-1 if x>0 else -1
  y_left = y-1 if y>0 else -1
  x_right = x+1 if x<m else m
  y_right = y+1 if y<n else n

  adjmatrix = [i for i in np.array(((x_left,y),(x,y_left),(x_right,y),(x,y_right)))]
  return [v for i,v in enumerate(adjmatrix) if (-1 not in v) and (m != v[0]) and (n != v[1])]

def check_instability(board,pos:tuple):
  unstable_pos = np.unique(instability_pos(board))
  m,n = board.shape
  corner = np.array([i for i in unstable_pos if (i[0]==0 and i[1]==0) or  (i[0]==m-1 and i[1]==0) or (i[0]==0 and i[1]==n-1) or (i[0]==m-1 and i[1]==n-1) ])
  mask = np.isin(unstable_pos,corner,invert=True)
  edge = unstable_pos[mask]
  return 1 if pos in [tuple(i) for i in corner] else 2 if pos in [tuple(j) for j in edge] else 3

def instability_pos(board):
  m,n=board.shape
  r,c = np.indices((m,n))
  arr = np.array([*zip(r.ravel(),c.ravel())],dtype=('i,i')).reshape(board.shape)
  return np.concatenate((arr[0,:],arr[:,0],arr[-1,:],arr[:,-1]),axis=0)
