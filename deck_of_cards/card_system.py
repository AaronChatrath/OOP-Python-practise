import random

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show_card(self):
        print(f"{self.value} of {self.suit}")

class Deck:

    #initialise class and build deck when instance is created
    def __init__(self):
        self.card_value_arr = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
        self.deck_of_cards = []
        self.build()
        self.shuffle()  
    
    def build(self):
        #using a nested for loop to build the deck of cards
        for i in ["Spades", "Clubs", "Hearts", "Diamonds"]:
            for j in self.card_value_arr:
                self.deck_of_cards.append(Card(i, j))

    def show_all(self):
        for c in self.deck_of_cards:
            c.show_card()
        print(len(self.deck_of_cards))
    
    def shuffle(self):
        for i in range(len(self.deck_of_cards)-1):
            r = random.randint(0,len(self.deck_of_cards)-1)
            self.deck_of_cards[i], self.deck_of_cards[r] = self.deck_of_cards[r], self.deck_of_cards[i]

    def draw_card(self):
        return self.deck_of_cards.pop()  
            

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.val_hand = []
    
    def draw(self,deck):
        self.hand.append(deck.draw_card())
        return self
    
    def show_val_hand(self):
        for c in self.val_hand:
            print(c)
    
    def populate_val_hand(self):
        for c in self.hand:
            self.val_hand.append(c.value)

class Computer(Player):
    def __init__(self,name):
        super().__init__(name)

class High_hand:

    def __init__(self, deck, player_1, player_2):
        self.deck = deck
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_1_sum = 0
        self.player_2_sum = 0
        self.values = {"2": 2, "3":3, "4":4, "5": 5, "6": 6, "7": 7, "8":8, "9":9, "10":10, "Jack": 10,
                 "Queen": 10, "King": 10, "Ace": 11}
    
    def start_game(self):
        for i in range(2):
            self.player_1.draw(self.deck)
            self.player_2.draw(self.deck)
        self.player_1.populate_val_hand()
        self.player_2.populate_val_hand()

    def show_hands(self):
        self.player_1.show_val_hand()
        self.player_2.show_val_hand()
    
    def calc_current_hand(self):
        for c in self.player_1.val_hand:
            self.player_1_sum += self.values[c]
            #print(c)
        print(self.player_1_sum)
        for c in self.player_2.val_hand:
            self.player_2_sum += self.values[c]
        print(self.player_2_sum) 

    def higher_hand(self):
        if self.player_1_sum > self.player_2_sum:
            print(f"{self.player_1.name} wins")
        elif self.player_2_sum > self.player_1_sum:
            print(f"{self.player_2.name} wins")
        else:
            print("It is a draw")


if __name__ == "__main__":
    c1 = Card("spade", "2")
    d1 = Deck()
    p1 = Player("harry")
    dealer = Player("dealer")
    high_hand = High_hand(d1,p1,dealer)
    high_hand.start_game()
    high_hand.calc_current_hand()
    high_hand.higher_hand()
