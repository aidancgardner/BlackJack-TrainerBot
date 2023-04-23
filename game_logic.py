# AIDAN GARDNER MARCH 20, 2023

import random

# Card Class
class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.name = value + '_of_' + suit

# Deck Class
class Deck:

    def __init__(self):
        self.cards = []
        self.build()

    # assembles the deck
    def build(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    # shuffles the deck
    def shuffle(self):
        random.shuffle(self.cards)

    # deals one card from the deck
    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return None # deck is empty
        
# Strategy Class
# input the hand of the dealer and the player
# the output will be the correct move that follows basic strategy
# according to https://www.blackjackinfo.com/card/basic-strategy-card-instructions/
class Strategy:

    def __init__(self, dealer_card, player_card1, player_card2):
        self.dealer_card = dealer_card
        self.player_card1 = player_card1
        self.player_card2 = player_card2

    def correct_choice(self):
        # outputs the correct choice based on the strategy chart
        # outputs: 'Hit', 'Stand', 'Double', 'Split'
        # other than what chart determines: always split aces, eights and twos
        output_map = {'S': 'Stand', 'H': 'Hit', 'D': 'Double'}
        if self.player_card1.value == 'ace' and self.player_card2.value == 'ace':
            return 'Split'
        elif self.player_card1.value == '8' and self.player_card2.value == '8':
            return 'Split'
        elif self.player_card1.value == '2' and self.player_card2.value == '2':
            return 'Split'
        elif self.player_card1.value == 'ace' or self.player_card2.value == 'ace':
            return output_map.get(self.soft_hand())
        else:
            return output_map.get(self.hard_hand())
    
    def soft_hand(self):
        chart = [
    # Dealer: 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | A   # Player:
            ['H','H','H','D','D','H','H','H','H','H'], # A,2
            ['H','H','D','D','D','H','H','H','H','H'], # A,3
            ['H','H','D','D','D','H','H','H','H','H'], # A,4
            ['H','H','D','D','D','H','H','H','H','H'], # A,5
            ['H','D','D','D','D','H','H','H','H','H'], # A,6
            ['S','S','S','S','S','S','S','H','H','H'], # A,7
            ['S','S','S','S','S','S','S','S','S','S'], # A,8
            ['S','S','S','S','S','S','S','S','S','S']  # A,9
        ]

        high_cards = ['ace', 'jack', 'queen', 'king']
        # get chart column
        if self.dealer_card.value in high_cards:
            if self.dealer_card.value == 'ace':
                dealer_idx = 9
            else:
                dealer_idx = 8
        else:
            dealer_idx = int(self.dealer_card.value) - 2

        # if black jack return stand as choice
        if self.player_card1.value in high_cards and self.player_card2.value in high_cards:
            return 'S'
        # if black jack with a 10
        if self.player_card1.value in  high_cards and self.player_card2 == '10':
            return 'S'
        if self.player_card2.value in  high_cards and self.player_card1 == '10':
            return 'S'
        
        # get chart row
        if self.player_card1.value == 'ace':
            player_idx = int(self.player_card2.value) - 2
        else:
            player_idx = int(self.player_card1.value) - 2
        return chart[player_idx][dealer_idx]
    
    def hard_hand(self):
        chart = [
    # Dealer: 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | A   # Player:
            ['H','H','H','H','H','H','H','H','H','H'], # 5
            ['H','H','H','H','H','H','H','H','H','H'], # 6
            ['H','H','H','H','H','H','H','H','H','H'], # 7
            ['H','H','H','H','H','H','H','H','H','H'], # 8
            ['D','D','D','D','D','H','H','H','H','H'], # 9
            ['D','D','D','D','D','D','D','D','H','H'], # 10
            ['D','D','D','D','D','D','D','D','D','D'], # 11
            ['H','H','S','S','S','H','H','H','H','H'], # 12
            ['S','S','S','S','S','H','H','H','H','H'], # 13
            ['S','S','S','S','S','H','H','H','H','H'], # 14
            ['S','S','S','S','S','H','H','H','H','H'], # 15
            ['S','S','S','S','S','H','H','H','H','H'], # 16
            ['S','S','S','S','S','S','S','S','S','S'], # 17
            ['S','S','S','S','S','S','S','S','S','S'], # 18
            ['S','S','S','S','S','S','S','S','S','S'], # 19
            ['S','S','S','S','S','S','S','S','S','S']  # 20
        ]

        high_cards = ['ace', 'jack', 'queen', 'king']
        # get chart column
        if self.dealer_card.value in high_cards:
            if self.dealer_card.value == 'ace':
                dealer_idx = 9
            else:
                dealer_idx = 8
        else:
            dealer_idx = int(self.dealer_card.value) - 2

        # get chart row
        if self.player_card1.value in high_cards:
            card_1_val = 10
        else:
            card_1_val = int(self.player_card1.value)
        if self.player_card2.value in high_cards:
            card_2_val = 10
        else:
            card_2_val = int(self.player_card2.value)
        player_idx = card_1_val + card_2_val - 5
        return chart[player_idx][dealer_idx]
