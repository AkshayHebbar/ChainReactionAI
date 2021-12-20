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
1.  Python - version 3.8
1.	Numpy
2.  Pytorch
2.	Matplotlib
3.	TextWrap

Links

References used from :

Author: Katz, Garrett
Topic : Minimax Game Trees, Neural Networks
Syracuse University
https://colab.research.google.com/drive/1YR8HjSw8K0n684S_oGnZPpU69SmOw355?usp=sharing#scrollTo=N6kj91QAfbuW
https://colab.research.google.com/drive/1JhOppwXwm47yk-AK7y7L5WTaaNDgCWXD?usp=sharing#scrollTo=TtHr_xOA7fa7

How to run the program?

STEP 1: Clone / Download code from our Github repo and decompress the file.
STEP 2: Open terminal on user’s system.
STEP 3: Go to the ChainReaction folder and run the “chain_reaction.py” ($ python chain_reaction.py).
STEP 4: Select if you want to play the game with a Human, Baseline AI or Tree Based AI by inputting the corresponding number.
*Implementation of Tree Based AI is in progress*
STEP 5: Play the game!


Since the game is interactive based on graphical displays, a Windows based machine would be ideal to run the game.
This has been tested using the following configurations:
OS: Windows
IDE: Python IDLE 3.8 64x
RAM: 16 GB
Disk Space: 250KB


IMPORTANT NOTE!

If the game is being run on a Windows system, make no changes to the code. If the game is being run on a Macintosh System, make the following changes in ‘print_board.py’ under display.
Comment the lines plt.ion(), plt.pause(5) and plt.close() except  plt.show(block = False). 
