import random

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
         'Queen':12, 'King':13, 'Ace':14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.allCards = []

        for suit in suits:
            for rank in ranks:
                #create card object
                createdCard = Card(suit, rank)
                self.allCards.append(createdCard)

    def shuffle(self):
        random.shuffle(self.allCards)

    def dealOne(self):
        return self.allCards.pop()

class Player:

    def __init__(self, name):
        self.name = name
        self.allCards = []

    def removeOne(self):
        return self.allCards.pop(0)
    def addCards(self, newCards):
        if type(newCards) == type([]): #If there is more than 1 new card to be added
            self.allCards.extend(newCards)
        else:
            self.allCards.append(newCards) #If there is only 1 new card to be added

    def __str__(self):
        return f'Player {self.name} has {len(self.allCards)} cards.'

playerOne = Player("One")
playerTwo = Player("Two")

newDeck = Deck()
newDeck.shuffle()

for x in range(26):
    playerOne.addCards(newDeck.dealOne())
    playerTwo.allCards(newDeck.dealOne())

gameOn = True
roundNum = 0
while gameOn:
    roundNum += 1
    print(f'Round {roundNum}')

    if len(playerOne.addCards()) == 0:
        print('Player One, out of cards! Player Two Wins!')
        gameOn = False
        break

    if len(playerTwo.addCards()) == 0:
        print('Player Two, out of cards! Player One Wins!')
        gameOn = False
        break

    #Start new round
    playerOneCards = []
    playerOneCards.append(playerOne.removeOne())
    playerTwoCards = []
    playerTwoCards.append(playerTwo.removeOne())

    #While at war
    
