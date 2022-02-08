values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
         'Queen':12, 'King':13, 'Ace':14}

class Card:
    def __init__(self, suit, rank):
        Card.suit = suit
        Card.rank = rank
        Card.value = values[rank]

    def __str__(self):
        return Card.rank + " of " + Card.suit

twoHearts = Card('Hearts', 'Two')
threeClubs = Card('Clubs','Three')

print(twoHearts.value)

print(twoHearts.value < threeClubs.value)
