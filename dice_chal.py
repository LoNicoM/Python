# code for dice challenge
#  ●┌┐└┘─│   chars
from random import randint


def get_rolls():
    while True:
        num_of_rolls = input("How many dice would you like to roll? [1 - 6]")
        if num_of_rolls.isdigit():
            num_of_rolls = int(num_of_rolls)
            if 0 < num_of_rolls < 7:
                rolls = [randint(0, 5) for _ in range(num_of_rolls)]
                return rolls
            else:
                print("Between 1 and 6 please!")
        else:
            print("Next time enter a number, OK?")


def print_dice(rolls):
    # put all dice pieces into a 2D array.
    dice = [
        ['┌───────┐', '│       │', '│   ●   │', '│       │', '└───────┘'],
        ['┌───────┐', '│ ●     │', '│       │', '│     ● │', '└───────┘'],
        ['┌───────┐', '│ ●     │', '│   ●   │', '│     ● │', '└───────┘'],
        ['┌───────┐', '│ ●   ● │', '│       │', '│ ●   ● │', '└───────┘'],
        ['┌───────┐', '│ ●   ● │', '│   ●   │', '│ ●   ● │', '└───────┘'],
        ['┌───────┐', '│ ●   ● │', '│ ●   ● │', '│ ●   ● │', '└───────┘']]

    print("Here are your dice rolls!")
    for i in range(5):
        for ii in rolls:
            print(dice[ii][i], end=" ")
        print("")


if __name__ == "__main__":
    print_dice(get_rolls())
