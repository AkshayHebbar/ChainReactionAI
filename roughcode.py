# Insert any rough code or module which can be used in the program


Structure:

Board.py
- Board = Returns the empty board
- valid states = Returns the empty locations + current players states
- opponent states in proximity = returns the opponent orbs nearby

populateAtom.py
- insertAtom = inserts atom at a particular location on the board and returns the board
- createChain = creates a chain reaction if present and returns the final state of the board

AI
- Minimax = provides the utilities after playing minimax algo
- Baseline AI = random actions
- human = call valid states and print the options

Display board
- print board
- print atoms/orbs at a particular location.