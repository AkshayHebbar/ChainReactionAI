from CreateBoard.create_board import init
from Display.print_board import print_board
from PlayGame.play_game import insert_atom
from Util.utilities import *
from Backend.cr_minimax import treeAI

def start_game(opponent:int):
    # implement functionality for opponent
    size = [int(x) for x in input("enter the size of board (>(1,2)) you want to play : ").split()]
    # valid_board = True if m>2 or n > 2
    # if valid_board:
    if size:
        m,n = size
        board,player = init(m,n)
    else:
        start_game(opponent)
    print_board(board, player)
    turn_count = 0
    won = 0
    while(not game_over(board,np.negative(player))):
        won = 1 if player>0 else 2
        turn_count+=1
        if (opponent == 3 and player == -1):
            max_depth = 2
            print("TreeAI Playing...")
            board,player = treeAI(board,player)
            print("Implement Tree Based AI")
        elif (opponent == 2 and player == -1):
            valid_pos = valid_states(board,player)
            index = np.random.choice([i for i,v in enumerate(valid_pos)])
            print("choosing pos:", valid_pos[index])
            pos = (valid_pos[index][0],valid_pos[index][1])
        else:
            position = [int(x) for x in input(f"player{won} enter the position of your atom : ").split()]
            if position:
                pos = (int(position[0]), int(position[1]))
            else:
                pos = (-1,-1)
        if(pos in valid_states(board,player)):
            board, player = insert_atom(board,pos,player)
            
    print(f"Game Over ! player {won} won")
