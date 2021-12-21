from CreateBoard.create_board import init
from Display.print_board import print_board
from PlayGame.play_game import insert_atom
from Util.utilities import *
from Backend.cr_minimax import treeAI

def start_game(opponent:int):
    # implement functionality for opponent
    size = [int(x) for x in input("enter the size of board (>(1,2)) you want to play | m n : ").split()]
    # valid_board = True if m>2 or n > 2
    # if valid_board:
    if size:
        m,n = size
        board,player = init(m,n)
    else:
        start_game(opponent)
    #printboard = print_state(board,player)
    print_board(board, player)
    turn_count = 0
    won = 0
    node_count = 0
    while(not game_over(board,np.negative(player))):
        #print(player)
        #print(board)
        won = 1 if player>0 else 2
        turn_count+=1

        if (opponent == 4 and player == -1):
            print("CNN")
        if (opponent == 3 and player == -1):
            input("Press Enter to continue...")
            print("TreeAI Playing...")
            max_depth = 2
            pos,nodes = treeAI(board,player)
            node_count +=nodes
            if pos not in [(x,y) for x,y in valid_states(board,player)]:
                valid_pos = valid_states(board,player)
                index = np.random.choice([i for i,v in enumerate(valid_pos)])
                pos = (valid_pos[index][0],valid_pos[index][1])
            print("Player 2 choosing pos:", pos)
        elif (opponent == 2 and player == -1):
            valid_pos = valid_states(board,player)
            index = np.random.choice([i for i,v in enumerate(valid_pos)])
            print("Player 2 choosing pos:", valid_pos[index])
            pos = (valid_pos[index][0],valid_pos[index][1])
            input("Press Enter to continue...")
        else:
            print("\nBoard:\n",board)
            print("Choose Valid Actions | p1 p2:",valid_states(board,player))
            position = [int(x) for x in input(f"player{won} enter the position of your atom : ").split()]
            if position:
                pos = (int(position[0]), int(position[1]))
            else:
                pos = (-1,-1)
        if(pos in valid_states(board,player)):
            board, player = insert_atom(board,pos,player)
            #printBoard = print_state(board,player)
            
            print_board(board,np.negative(player))

    score = board.sum()
    print(f"Game Over ! player {won} won\nYour score is {score}")
    print("********** Thank you for playing **********")
