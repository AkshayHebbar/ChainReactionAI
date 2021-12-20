#Author: Srinidhi Shivaram
from PlayGame.game import start_game
from PlayGame.simulate import simulate_game
from PlayGame.batch import simulate


# Created Main function for restarting game
def main():
    gameplay = input("Choose option: 1. Play Game 2. Simulate vs Baseline: ")
    if int(gameplay) == 1:
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
    else:
        ai = input("Choose AI:  1.TreeBasedAI 2.TreeAI+NN: ")
        ai_choice= int(ai)
        if ai_choice in range(1,3):
            simulate(ai_choice)
            #simulate_game(ai_choice)
        
if __name__ == "__main__":
    main() # Calling main method in Main thread
