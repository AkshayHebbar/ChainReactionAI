READ ME:

# ChainReactionAI
A chain reaction game based on AI


References:

1. Minimax Algorithm
2. Numpy Documentation
3. Matplotlib Documentation
4. TextWrap Documentation

Dependencies Used:

For Chain Reaction the following are utilized
1.	Numpy
2.	Matplotlib
3.	TextWrap

How to run the program?

STEP 1: Clone / Download code from our Github repo and decompress the file.
STEP 2: Open terminal on user’s system.
STEP 3: Go to the ChainReaction folder and run the “chain_reaction.py” ($ python chain_reaction.py).
STEP 4: Select if you want to play the game with a Human, Baseline AI or Tree Based AI by inputting the corresponding number.
*Implementation of Tree Based AI is in progress*
STEP 5: Play the game!

IMPORTANT NOTE!

If the game is being run on a Windows system, make no changes to the code. If the game is being run on a Macintosh System, make the following changes in ‘print_board.py’ under display.
Comment the lines plt.ion(), plt.pause(5) and plt.close() except  plt.show(block = False). 
