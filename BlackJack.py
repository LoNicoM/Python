# BlackJack By Leon Mailfert
import random
import os
'''
NOTE THIS GAME IS FAR FROM FINISHED!

This project was inspired by playing Red Dead Redemption 2
I plan to implement a console based BlackJack game.
this is my first game development see where it goes from here
perhaps i will fall on my face, or perhaps I will succeed
it all depends on my commitment. ♦♥♣♠

'''
clear = lambda: os.system('cls')

def buildDeck(): # builds a list and shuffles the result ♦♥♣♠
    suits = ("♥", "♦", "♣", "♠")
    cards = ("A",) + tuple(range(2,11)) + ("J", "Q", "K")
    d = []
    for i in suits:
        for j in cards:
            d.append(f"[{j} {i}]") if j != 10 else d.append(f"[{j}{i}]")
    random.shuffle(d)
    return d
4
def getNoPlayers(): # keep asking until we get a valid response
    while True:
        x = input("How many players are there [1-4]: ")
        if x.isdigit() and (int(x) in range(1,5)):
            break
        else:
            print("Try Again!")
    return int(x)

def dealCard(): # deal a card from top of deck then remove from deck
    y = deck[0]
    deck.pop(0)
    return y

def dealHand():
    for i in range(2): # deal 2 cards to each player sequentially 
        for j in range(noPlyrs):
            hands[j].append(dealCard())
        hands[4].append(dealCard()) # dealer card

def calcScore(x): # will probably redo this later to use a dictionary
    y = 0
    for z in x:
        if z[1].isdigit(): # check if its a digit
            y += 10 if int(z[1]) == 1 else int(z[1])
        elif z[1] != "A": # everythin else except ace
            y += 10
        elif z[1] == "A": # ace
            y += 11
    for w in x:
        if y > 21 and w[1] == "A": # check if score is over 21 and deduct 10 for each ace
            y -= 10
    return y

def calcAllScores(): # calc all scores initially 
    scores.clear()
    for i in range(5):
        scores.append(calcScore(hands[i]))

def displayTable(stage = 0):
    dlrHide =  hands[4][1] if (scores[4] == 21) or stage == 1 else "[▓▓▓]"
    dlrScore = scores[4]  if (scores[4] == 21) or stage == 1 else scores[4] - calcScore([" 0",hands[4][1]]) # a bit hacky bad implementation
    clear()
    print("|          | SCORE |")
    print("| Dealer   | {:>5} | {} {} ".format(dlrScore, hands[4][0], dlrHide), end="")
    if stage == 1:
        for k in range(len(hands[4][2:])):
            print("{:^4} ".format(hands[4][k + 2]), end="")
        if scores[4] > 21:
            print("BUST!", end="")
    if scores[4] == 21:
        print("BLACKJACK!", end="")
    print("")
    for i in range(noPlyrs):
        print("| Player {} | {:>5} | ".format(i + 1, scores[i]), end="")
        for j in range(len(hands[i])):
            print("{:^4} ".format(hands[i][j]), end="")
        if scores[i] > 21:
            print("BUST!", end="")
        if scores[i] == 21 and len(hands[i]) == 2:
            print("BLACKJACK!", end="")
        print("")

def hitStand(p):
    while True: # get input loop, keep asking until valid answer is given
        c = input("Player {}, [H]it or [S]tand: ".format(p+1))
        c = c.upper()
        if c == "H" or "S":
            break
        else:
            print("Try Again!")
    if c == "H":
        hands[p].append(dealCard()) # add a card to players hand
        scores[p] = calcScore(hands[p])# update score
        return True
    elif c == "S":
        return False

def playersTurn():
        for i in range(noPlyrs): # repeat this for the number of players
            turn = True if scores[4] != 21 else False
            while turn: # run this loop until while its the players turn
                if scores[i] >= 21: # 
                    turn = False
                    continue
                turn = hitStand(i)
                displayTable()

def dealerTurn():
    displayTable(1) # Stage 1 is dealers turn
    while True: # keep doing this until dealer score is > 17
        if scores[4] < 17: # dealer must hit if his score is less than 17
            hands[4].append(dealCard())
            scores[4] = calcScore(hands[4])
        else:
            break
    displayTable(1)
            
    
def runGame(): # TODO make a loop to run the game
    global noPlyrs
    global deck
    global hands
    global scores
    hands = []
    scores = []
    for i in range(5): hands.append([])# build a list of lists to store hands iterable and indexable
    noPlyrs = getNoPlayers() # get num players from console
    deck = buildDeck() # call the function to generate the deck and store in global variable deck
    #takeBets() # TODO implement betting function
    dealHand() # deal cards deals one card to each player in a circle similar to real blackjack
    calcAllScores() # get initial scores
    displayTable() # output hands and scores to console
    playersTurn() # ask players what they want to do
    dealerTurn() # Dealer has his turn
    #calcWinners() # Calculate winners and pay dividends

runGame()
#print("There are {} cards left in the deck.".format(len(deck))) # debug

'''


'''
