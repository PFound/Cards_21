import random

class deck(object):
    def __init__(self):
        self.deck = []
        self.dealt = [] #Prevents from dealing the same card
        self.PopulateDeck()
        
    def PopulateDeck(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        for suit in suits:
            for rank in range(2, 15):
                if rank == 11:
                    value = "Jack"
                elif rank == 12:
                    value = "Queen"
                elif rank == 13:
                    value = "King"
                elif rank == 14:
                    value = "Ace"
                else:
                    value = str(rank)

                self.deck.append(Card(rank, value, suit))

    def deal(self, players, cards):
      #Randomly select card
      remaining_cards = [card for card in self.deck if card not in self.dealt]
      card_index = random.randrange(0, len(remaining_cards)-1)
      card = remaining_cards[card_index]
      self.dealt.append(card)
      return card
    
    def shuffle(self):
        self.dealt = []

        
class Card(object):
  
    def __init__(self, num, rank, suit):
        self.rank = rank
        self.num = num       
        self.suit = suit
        self.card = str(self.rank) + " " + str(self.suit)
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit and self.num == other.num
      

Gamedeck = deck()      
Gamedeck.startGame

print len(Gamedeck.dealt)
#And here you will compare the cards to see if the player wins or not. Not sure 
#what exact criterion you're using.

#deck.shuffle() #And leave your deck nicely shuffled for next game
for c in Gamedeck.dealt:
  print c.rank
  print c.suit
  print c.card
  print c.num


