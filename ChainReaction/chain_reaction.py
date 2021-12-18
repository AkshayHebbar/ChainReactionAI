from PlayGame.game import *

# Created Main function for restarting game
def main():
    print("Choose your opponent :")
    choice = input("1.Human 2.BaselineAI 3.TreeBasedAI 4. TreeBaseAI+NN: ")
    # Check if input is not null
    if choice:
        opponent = int(choice)
        if opponent in range(1,5):
            start_game(opponent)
        else:
            print("Invalid Input! Restarting Game...")
            main()
    else:
        #Added code for restart
        print("Invalid Input! Restarting Game...")
        main()

if __name__ == "__main__":
    main() # Calling main method in Main thread
