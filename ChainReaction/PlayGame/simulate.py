from CreateBoard.create_board import init
from Display.print_board import print_board
from PlayGame.play_game import insert_atom
from Util.utilities import *
from Backend.cr_minimax import treeAI
from Backend.neural_net import dl_minimax,nn_eval

def simulate_game(opponent:int,size):
    # implement functionality for opponent
    #size = [int(x) for x in input("enter the size of board (>(1,2)) you want to play : ").split()]

    if size:
        m,n = size
        board,player = init(m,n)
    else:
        simuate_game(opponent)
        
    print_board(board, player)
    turn_count = 0
    won = 0
    node_count = 0
    while(not game_over(board,np.negative(player))):
        #print("player:",player)
        #print(board)
        won = 1 if player>0 else 2
        turn_count+=1
        
        if (opponent == 2 and player == -1):
            print("CNN Choosing pos")
            nodecount = 0
            _, a, nodes = dl_minimax((board,player), 2, nn_eval)
            pos = [(x,y) for x,y in valid_states(board,player)][a]
            codecount+=nodes
        elif (opponent == 1 and player == -1):
            max_depth = 2
            pos,nodes = treeAI(board,player)
            node_count +=nodes
            if pos not in [(x,y) for x,y in valid_states(board,player)]:
                valid_pos = valid_states(board,player)
                index = np.random.choice([i for i,v in enumerate(valid_pos)])
                pos = (valid_pos[index][0],valid_pos[index][1])
            print("TreeAI choosing pos:", pos)
            #input("Press Enter to continue...")
        else:
            valid_pos = valid_states(board,player)
            index = np.random.choice([i for i,v in enumerate(valid_pos)])
            print("BaseLineAI choosing pos:", valid_pos[index])
            pos = (valid_pos[index][0],valid_pos[index][1])
            #input("Press Enter to continue...")
        if(pos in valid_states(board,player)):
            board, player = insert_atom(board,pos,player)
            #printBoard = print_state(board,player)
            print_board(board,np.negative(player))

    score = board.sum()
    print(f"Game Over ! player {won} won\nYour score is {score}")
    print("********** Thank you for playing **********")
    return node_count,abs(score)
