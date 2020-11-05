# code for dice challenge
#  ●┌┐└┘─│   chars
from random import randint


def get_rolls():
    while True:
        num_of_rolls = input("How many dice would you like to roll? ")
        if num_of_rolls.isdigit():
            num_of_rolls = int(num_of_rolls)
            if num_of_rolls > 0:
                rolls = [randint(0, 5) for _ in range(num_of_rolls)]
                rolls = [rolls[i:i + 6] for i in range(0, len(rolls), 6)]
                return rolls
            else:
                print("More than 0 please!")
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
    for iii in rolls:
        for i in range(5):
            for ii in iii:
                print(dice[ii][i], end=" ")
            print("")


if __name__ == "__main__":
    while True:
        print_dice(get_rolls())
        if input("again [y]?").lower() != "y":
            break
