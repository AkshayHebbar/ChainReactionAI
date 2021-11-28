import numpy as np

def create_board(m:int,n:int):
    return np.zeros((m,n),dtype=int)
    
def init(m,n):
    board = create_board(m,n)
    player = 1
    return (board,player)
    
