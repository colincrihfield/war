#! python3

import random

# Initialize decks
def initDeck(numSuits):
    deck = []
    for s in range(0, numSuits):
        for n in range(2, 15):
            deck.append(str(suits[s][0]) + str(n))
    return deck

# Split decks
def splitDeck():
    deckSize = len(fullDeck)
    p1Deck = fullDeck[0:int(deckSize/2)]
    p2Deck = fullDeck[int((deckSize/2)):deckSize]
    return p1Deck, p2Deck

# Cut suit out of string - getting just the number
def getNum(card):
    num = int(card[1:len(card)])
    return num

# Non-war action handling function
def noTie(warChest, p1Deck, p1Discard, p2Deck, p2Discard):
    p1Val = getNum(p1Deck[0])
    p2Val = getNum(p2Deck[0])
    # print cards - change this to a function ####################
#    printBoardCards(warChest, p1Deck, p1Discard, p2Deck, p2Discard)
#    input()
    # add to winner's deck
    if p1Val > p2Val:
        p1Discard.append(p1Deck[0])
        p1Discard.append(p2Deck[0])
        handWinner = 1
    else:
        p2Discard.append(p1Deck[0])
        p2Discard.append(p2Deck[0])
        handWinner = 2
    # delete from decks
    p1Deck.remove(p1Deck[0])
    p2Deck.remove(p2Deck[0])
    return handWinner, p1Deck, p1Discard, p2Deck, p2Discard

# Tie (war) action handling function
def tie(warChest, p1Deck, p1Discard, p2Deck, p2Discard):
    # print cards - same change to add print function
#    printBoardCards(warChest, p1Deck, p1Discard, p2Deck, p2Discard)
#    input()
    # move initial tie to war chest - doing separately to support print later
    warChest.append(p1Deck[0])
    warChest.append(p2Deck[0])
    p1Deck.remove(p1Deck[0])
    p2Deck.remove(p2Deck[0])
    p1Deck, p1Discard, p2Deck, p2Discard = reshuffle(p1Deck, p1Discard, p2Deck, p2Discard)
    # and 3 more to war chest
    for i in range(3):
        p1cardsleft = len(p1Deck) + len(p1Discard)
        if len(p1Deck) + len(p1Discard) > 1:
            warChest.append(p1Deck[0])
            p1Deck.remove(p1Deck[0])
        p2cardsleft = len(p2Deck) + len(p2Discard)
        if len(p2Deck) + len(p2Discard) > 1:
            warChest.append(p2Deck[0])
            p2Deck.remove(p2Deck[0])
        i = i + 1
        p1Deck, p1Discard, p2Deck, p2Discard = reshuffle(p1Deck, p1Discard, p2Deck, p2Discard)
#        printBoardCards(warChest, p1Deck, p1Discard, p2Deck, p2Discard)
#        input()
    # draw again
    p1Val = getNum(p1Deck[0])
    p2Val = getNum(p2Deck[0])
    if p1Val != p2Val:
        handWinner, p1Deck, p1Discard, p2Deck, p2Discard = noTie(warChest, p1Deck, p1Discard, p2Deck, p2Discard)
        if handWinner == 1:
            p1Discard = p1Discard + warChest
            warChest.clear()
            return warChest, p1Deck, p1Discard, p2Deck, p2Discard
        else:
            p2Discard = p2Discard + warChest
            warChest.clear()
            return warChest, p1Deck, p1Discard, p2Deck, p2Discard
    else:
        tie(warChest, p1Deck, p1Discard, p2Deck, p2Discard)
    
# Check for winner
def winCheck():
    if len(p1Deck) == 0 and len(p1Discard) == 0:
        return True, 'Player 2'
    elif len(p2Deck) == 0 and len(p2Discard) == 0:
        return True, 'Player 1'
    else:
        return False, 'None'

# Check for reshuffle and do so if necessary
def reshuffle(p1Deck, p1Discard, p2Deck, p2Discard):
    if len(p1Deck) == 0:
        p1Deck = p1Discard
        random.shuffle(p1Deck)
        p1Discard = []
    if len(p2Deck) == 0:
        p2Deck = p2Discard
        random.shuffle(p2Deck)
        p2Discard = []
    return p1Deck, p1Discard, p2Deck, p2Discard

# Print function with cards out
def printBoardCards(warChest, p1Deck, p1Discard, p2Deck, p2Discard):
    p1Card = cardDict[str(getNum(p1Deck[0]))] + ' of ' + suitsDict[p1Deck[0][0]]
    p2Card = cardDict[str(getNum(p2Deck[0]))] + ' of ' + suitsDict[p2Deck[0][0]]
    print('--------------------------')
    print('Player 1')
    print('Deck:   ', str(len(p1Deck) - 1), '       ', p1Card)
    print('Discard:', len(p1Discard))
    if len(warChest) == 0:
        print('++++++++++++++++++++++++++')
    else:
        print('+++++++++++++++++++ War Chest:', len(warChest))
    print('Player 2')
    print('Deck:   ', str(len(p2Deck) - 1), '       ', p2Card)
    print('Discard:', len(p2Discard))
    print('--------------------------')

# Print function without cards
def printBoardNoCards(warChest, p1Deck, p1Discard, p2Deck, p2Discard):
    print('--------------------------')
    print('Player 1')
    print('Deck:   ', len(p1Deck))
    print('Discard:', len(p1Discard))
    print('++++++++++++++++++++++++++')
    print('Player 2')
    print('Deck:   ', len(p2Deck))
    print('Discard:', len(p2Discard))
    print('--------------------------')
    
####### Main Game Loop #########
print('Start')

# Static sets
suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
suitsDict = {'H':'Hearts', 'D':'Diamonds', 'C':'Clubs', 'S':'Spades'}
cardDict = {'2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', '10':'10',
            '11':'Jack', '12':'Queen', '13':'King', '14':'Ace'}

print('1 for full mode, 2 for test')
mode = int(input())
if mode == 1:
    fullDeck = initDeck(4)
    print('Full Deck:', fullDeck)

    random.shuffle(fullDeck)
    print('Shuffled Deck:', fullDeck)

    p1Deck, p2Deck = splitDeck()

    print('p1 Deck:', p1Deck)
    print('p2 Deck:', p2Deck)

else:
    p1Deck = ['S5', 'H4', 'C12']
    p2Deck = ['H5', 'H6', 'H6', 'D8', 'D9', 'S10', 'C14']
    

p1Discard, p2Discard, warChest = [], [], []
handWinner = 0

handCount = 0

while True:
#    printBoardNoCards(warChest, p1Deck, p1Discard, p2Deck, p2Discard)
#    input()
    p1Val = getNum(p1Deck[0])
    p2Val = getNum(p2Deck[0])
    # no tie draw, handle actions
    if p1Val != p2Val:
        handWinner, p1Deck, p1Discard, p2Deck, p2Discard = noTie(warChest, p1Deck, p1Discard, p2Deck, p2Discard)
    else:
        warChest, p1Deck, p1Discard, p2Deck, p2Discard = tie(warChest, p1Deck, p1Discard, p2Deck, p2Discard)
    # check for winner
    win, winner = winCheck()
    handCount += 1
    if win:
        print('Game over,', winner, 'is the winner. It took:', handCount, 'hands.')
        break
    # reshuffle if necessary
    p1Deck, p1Discard, p2Deck, p2Discard = reshuffle(p1Deck, p1Discard, p2Deck, p2Discard)

print('End')
