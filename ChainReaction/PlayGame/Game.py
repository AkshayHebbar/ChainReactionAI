from CreateBoard.create_board import init
from Display.print_board import print_board
from PlayGame.play_game import insert_atom
from Util.utilities import *

def start_game(opponent:int):
    # implement functionality for opponent
    m,n = [int(x) for x in input("enter the size of board (>(1,2)) you want to play : ").split()]
    # valid_board = True if m>2 or n > 2
    # if valid_board:
    board,player = init(m,n)
    print_board(board, player)
    turn_count = 0
    won = 0
    while(not game_over(board,player*-1)):
        won = 1 if player>0 else 2
        turn_count+=1
        position = [int(x) for x in input("enter the position of your atom : ").split()]
        pos = (int(position[0]), int(position[1]))
        if(pos in valid_states(board,player)):
            board, success = insert_atom(board,pos,player)
            if success:
                player = player*(-1)
    print(f"Game Over ! player {won} won")
