# A very early prototype battleship game, maybe ill finish it one day
# generates a random field of battleships, not much else

import numpy as np
from random import randint



class shownField:
    " displayed stuff "
    def __init__(s, grid, qtys): #take 1 input arguement
        s.grid = grid
        s.qtys = qtys # (4long,3long,2long,1long) qtys of length
        s.field = np.empty(grid, dtype=str)
                        
    def displayGrid(s): # display the
        for i in range(s.grid[0]):
            print("   {}".format("".ljust(s.grid[0]*4+1,"═")))
            print("{:<3}".format(i + 1), end="")
            for j in range(s.grid[1]):
                print("║ {:1} ".format(s.field[i, j]), end="")
            print("║")
        print("   {}".format("".ljust(s.grid[0]*4+1,"═")))
        print("   ", end="")
        for i in range(s.grid[1]):
            print("  {:1} ".format(chr(65 + i)), end="")
        print("")

class hiddenField(shownField):
    " behind the scenes stuff "
    def getRandCord(s, length):
        while True:
            row = randint(1,s.grid[0] - length) #row
            col = randint(1,s.grid[1] - length) #column
            dir_ = randint(0,1) # direction 0 = horiz y = vert
            # check for overlaps    
            if dir_ == 0 and not (s.field[row-1:row+2, col-1:col+length+2] == "O").any():
                return (row, col, dir_)
            elif dir_ == 1 and not (s.field[row-1:row+length+2, col-1:col+2] == "O").any():
                return (row, col, dir_)               
            else:
                continue
            break

    def populateArray(s):
        lengths = (4,3,2,1)
        for i in range(len(lengths)):
            for j in range(s.qtys[i]):
                cord = s.getRandCord(lengths[i])
                print(cord) # Debug
                if cord[2] == 0:
                    s.field[cord[0], cord[1]:cord[1] + lengths[i] + 1] = "O"
                else:
                    s.field[cord[0]:cord[0] + lengths[i] + 1, cord[1]] = "O"
        

def runGame(): # the sequence of events
    grid = (10,10)
    quantities = (1,2,3,4) # (4's, 3's, 2's , 1's)
    shown = shownField(grid, quantities)
    hidden = hiddenField(grid, quantities)
    
    hidden.populateArray()
#   shown.displayGrid()
    hidden.displayGrid() #debug


runGame() # start here