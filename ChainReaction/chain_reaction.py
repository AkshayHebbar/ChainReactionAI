from PlayGame.Game import *

if __name__ == "__main__":
    print("Choose your opponent :")
    opponent = input("1.Human 2.BaselineAI 3.TreeBasedAI : ")
    start_game(opponent)