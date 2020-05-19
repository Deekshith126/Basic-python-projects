from random import randint
from IPython.display import clear_output

class BlackJack():
    def __init__(self):
        self.deck=[]
        self.suits = ('Spades','Hearts','Diamonds','Clubs')
        self.values = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'Q', 'K', 'J', 'A')
        
    def makeDeck(self):   # create a method that creates a deck of 52 cards, each card should be a tuple with a value and suit 
        for suit in self.suits:
            for value in self.values:
                self.deck.append((value,suit))
    
    def pullCard(self):  # method to pop a card from deck using a random index value
        return self.deck.pop(randint(0, len(self.deck)-1))
		
game = BlackJack()
game.makeDeck()


# create a class for the dealer and player objects 
class Player():
    def __init__(self,name):
        self.name = name
        self.hand = []
        
        
    def addCard(self, card):
        self.hand.append(card)
        
    def showHand(self,dealer_start = True):   # if not dealer's turn then only show one of his cards, otherwise show all 
        print('\n {}'.format(self.name))
        print('=============')
        for i in range(len(self.hand)):
            if self.name == 'Dealer' and i==0 and dealer_start:
                print('_ of _')
            else:
                card = self.hand[i]
                print('{} of {}'.format(card[0],card[1]))
                
                
    def calcHand(self,dealer_start = True): # if not dealer's turn then only give back total of second card
        total = 0
        aces = 0
        card_values = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'K':10, 'Q':10, 'A':11}
        if self.name =='Dealer' and dealer_start:
            card = self.hand[1]
            return card_values[card[0]]
        for card in self.hand:
            if card[0]=='A':
                aces+=1
            else:
                total += card_values[card[0]]
        for i in range(aces):
            if total + aces > 21:
                total += 1
            else:
                total +=11
        return total
		
		
name = input('What is your name: ')
clear_output()
player = Player(name)
dealer = Player('Dealer')
# print(player.name, dealer.name)

for i in range(2):  # add two cards to the dealer and player hand 
    player.addCard(game.pullCard())
    dealer.addCard(game.pullCard())
	
	
player.showHand()
dealer.showHand()

player_bust = False   # variable to keep track of player going over 21 
while input('Would you like to stay or hit?').lower()!='stay':
    clear_output()
    player.addCard(game.pullCard())
    player.showHand()
    dealer.showHand()
    if player.calcHand() > 21:
        player_bust = True
        #print('You lose!')
        break
		
# handling the dealer's turn, only run if player didn't bust 
dealer_bust = False
if not player_bust:
    while dealer.calcHand(False) < 17:  #  pass False to calculate all cards 
        # pull card and put into player's hand 
        dealer.addCard(game.pullCard())
        if dealer.calcHand(False) > 21:
            dealer_bust = True
            #print('You win!!')
            break

clear_output()
player.showHand()
dealer.showHand(False)


#calcualte the winner
if player_bust:
    print('You busted better luck next time')
elif dealer_bust:
    print('The dealer busted, you win')
elif dealer.calcHand(False) > player.calcHand():
    print('Dealer has higher cards, you lose')
elif dealer.calcHand(False) < player.calcHand():
    print('Congrats!! You beat the dealer')
else:
    print('You pushed! No one wins')

