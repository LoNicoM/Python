# A very early prototype console battleship game, maybe ill finish it one day
# generates a random field of battleships, not much else

import numpy as np
from random import randint


class ShownField:
    """ displayed stuff """

    def __init__(self, grid, qtys):  # take 1 input arguement
        self.grid = grid
        self.qtys = qtys  # (4long,3long,2long,1long) qtys of length
        self.field = np.empty(grid, dtype=str)

    def display_grid(self):  # display the
        print("   ╔═══{}╗".format("╦═══" * (self.grid[0]-1)))
        for i in range(self.grid[0]):
            print(f"{i + 1:<3}", end="")
            for j in range(self.grid[1]):
                print("║ {:1} ".format(self.field[i, j]), end="")
            print("║")
            if i != self.grid[1] - 1:
                print("   ╠═══{}╣".format("╬═══" * (self.grid[0]-1)))
        print("   ╚═══{}╝\n   ".format("╩═══" * (self.grid[0]-1)), end="")
        for i in range(self.grid[1]):
            print("  {:1} ".format(chr(65 + i)), end="")
        print("")


class HiddenField(ShownField):
    """ behind the scenes stuff """

    def get_rand_cord(self, length):
        count = 0
        while True:
            row = randint(1, self.grid[0] - length)  # row
            col = randint(1, self.grid[1] - length)  # column
            dir_ = randint(0, 1)  # direction 0 = horiz y = vert
            # check for overlaps    
            if dir_ == 0 and not (self.field[row - 1:row + 2, col - 1:col + length + 2] == "▓").any():
                return row, col, dir_
            elif dir_ == 1 and not (self.field[row - 1:row + length + 2, col - 1:col + 2] == "▓").any():
                return row, col, dir_
            else:
                count += 1
                if count == 100:
                    return
                continue

    def populate_array(self):
        lengths = (4, 3, 2, 1)
        for i in range(len(lengths)):
            for j in range(self.qtys[i]):
                cord = self.get_rand_cord(lengths[i])
                try:
                    if cord[2] == 0:
                        self.field[cord[0], cord[1]:cord[1] + lengths[i] + 1] = "▓"
                    else:
                        self.field[cord[0]:cord[0] + lengths[i] + 1, cord[1]] = "▓"
                except TypeError:
                    self.field = np.empty(self.grid, dtype=str) # cant fit start again
                    self.populate_array()


def run_game():  # the sequence of events
    grid = (10, 10)
    quantities = (1, 2, 3, 4)  # (4's, 3's, 2's , 1's)
    # shown = ShownField(grid, quantities)
    hidden = HiddenField(grid, quantities)
    hidden.populate_array()
    # shown.displayGrid()
    hidden.display_grid()  # debug


run_game()  # start here
