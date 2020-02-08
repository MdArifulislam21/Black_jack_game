
import  random


# set the name of all the cards in suits
suits =  ('Hearts', 'Diamonds', "Spades", 'Clubs')

#set the rank 
ranks = ('Tow', 'Threee', 'Four', 'Five','Six', 'Seven', 'Eight', 'Nine','Ten', 'Jack',
         'Queen', 'King', "Ace")

# set the valaue of rank
values = {'Tow':2, 'Threee':3, 'Four':4, 'Five':5,'Six':6, 'Seven':7, 'Eight':8, 'Nine':9,'Ten':10,
         'Jack':10,  'Queen':10, 'King':10, "Ace":11}

# Create a variable playing and set as true.
playing = True

# Create Class Card
class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

# call the Card class and create object test_card
test_card = Card('Ace','Two')
print(test_card)


#Create Deck Class

class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))


    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp +='\n' + card.__str__()
        return  'The deck has :' + deck_comp

    # create a shuffle method
    def shuffle(self):
        random.shuffle(self.deck)

    # create a deal method
    def deal(self):
        single_card = self.deck.pop()
        return  single_card

# call the Deck class and create object test_deck
test_deck = Deck()
test_deck.shuffle()
print(test_deck)


# Create  Hand Class
class Hand():

    def __init__(self):
        self.cards =[]
        self.value = 0
        self.aces = 0

   # Create  add_class method
    def add_card(self, card):

        self.cards.append(card)
        self.value += values[card.rank]

        # track aces
        if card.rank == 'Ace':
            self.aces += 1

    # Create got_aces method
    def got_aces(self):
        while self.value >21 and self.aces:
            self.value -= 10
            self.aces -=10

# call the Hand class and create object test_player
test_player = Hand()
get_card = test_deck.deal()
print(get_card)
test_player.add_card(get_card)
print(test_player.value)


# Create Chips class
class Chips():
    def __init__(self, total=100):
        self.total = total
        self.bet = 0
    
    #create win_bet method
    def win_bet(self):
        self.total += self.bet

    #create lose_bet method
    def lose_bet(self):
        self.total -= self.bet


# create a take_bet function
def take_bet(Chips):
    while True:

        try:
            Chips.bet = int(input('How much would you like to place: '))

        except:
            print('Please provide an integer')

        else:
            if Chips.bet > Chips.total:
                print('You do not have chips')

            else:
                break

# create a hit function
def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.got_aces()

# create a hit_or_stand function
def hit_or_stand(deck, hand):
    global  playing
    while True:
        x = input('Hit or Stand? Enter h or s: ')

        if x =='h':
            hit(deck, hand)

        elif x == 's':
            print('Player wants to stand dealer turn')
            playing = False

        else:
            print("I don't understand, Please enter h, or s: ")
            continue
        break

# Create a show_some function
def show_some(player, dealer):
    print('\n Dealer Hand: ')
    print('<Card Hidden >')
    print('', dealer.cards[1])
    print("\n Player's Hand: ", *player.cards, sep = '\n')


# Create a show_some function
def show_all(player, dealer):
    print("\n Dealer's Hand: ", *dealer.cards, sep='\n')
    print("Dealers hand= ", dealer.value)
    print('\nplayers hand: ', *player.cards, sep='\n')
    print("player's hand= ", player.value)


# Win or lose decleration function

def player_wins(player, dealer, Chips):
    print('Player Win Yea!')
    Chips.win_bet()


def player_lose(player, dealer, Chips):
    print('Player Busted')
    Chips.lose_bet()


def dealer_wins(player, dealer, Chips):
    print('Dealer win')
    Chips.win_bet()


def dealer_lose(player, dealer, Chips):
    print('Dealer Busted')
    Chips.lose_bet()


def push(player, dealer, Chips):
    print("Its a Push")


# Logic Section for Game

while playing:

    print("Welcome to the Club")

    # Create  and shuffle
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())


    # Player Chips setup
    player_chips = Chips()

    # ask for bet
    take_bet(player_chips)

    #show cards
    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        # Criteria for 21 num check
        if player_hand.value >21:
            player_lose(player_hand, dealer_hand, player_chips)
            break

    # if player doesn't lose, ask dealer to play
    if player_hand.value >= 21:

        while dealer_hand.value  < player_hand.value:
            hit(deck, dealer_hand)

        # show all cards
        show_all(player_hand, dealer_hand)

        # code different winning scenarios
        if dealer_hand.value < 21:
            dealer_lose(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand, Chips)

        # inform the player about their sitution

        print(f'\n Player total chips are  {player_chips.total}')

        # Ask the player to play again
        new_game = input("Would you like to play [y/n]: ")

        if new_game[0].lower() == 'y':
            playing = True
            continue

        else:
            print("Thank You!, Don't play this game again!")
            break





















