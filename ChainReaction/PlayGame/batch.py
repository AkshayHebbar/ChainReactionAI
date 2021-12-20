#Author: Akshay Hebbar
import numpy as np
from PlayGame.simulate import simulate_game
import matplotlib.pyplot as pt

def simulate(opponent:int):
    print("simulating 100 events of TreeAI vs BaselineAI")
    if opponent ==1 :
        hist = [],[]
        for i in range(100):
            size = np.random.randint(2,5),np.random.randint(2,5)
            res = simulate_game(opponent,size)
            print(res)
            hist[0].append(res[0])
            hist[1].append(res[1])
            print(hist)
        pt.plot(hist[0], 'b-')
        pt.plot(hist[1], 'r-')
        pt.plot()
        pt.legend(["Nodes","Scores"])
        pt.show()   
        print("********** End of Simulation. Thank you for playing **********")

    else:
        print("Simulating 100 events of TreeNN_AI vs BaselineAI")
