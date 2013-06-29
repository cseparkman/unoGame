# coding:utf-8
#-------------------------------------------------------------------------------
#
# Author:      parkman
#
# Created:     28-06-2013
# Copyright:   (c) parkman 2013
# Licence:     <MIT>
#-------------------------------------------------------------------------------
import random

from utils.functions import *
from utils.unoCard import StandardCard

_player_list = ["player" + str(i) for i in range(5)]
_first_player = _player_list[0]
_default_card = StandardCard('r', 0)
_total_cards = cards

class UnoController(object):
    """
    The UnoController which handlers the request from the uno player;
    POST - The player play a uno card;
    Get - The player get a uno card [or muitiple cards];
    total_cards - The total uno cards
    punlist_number - In this cycle, the player need to be punlished for punlist_number cards
    Using Lists as Queues, example:
        queue.append;
        queue.popleft;
    """
    total_cards = _total_cards
    punlish_number = 0
    order = True
    player_list = _player_list
    current_player = _first_player
    current_card = _default_card

    def GET(self, player):
        '''
        The player will be punlished by the punlist_number cards
        '''
        punlish_cards = []
        for i in range(punlish_number):
            if not len(UnoController.total_cards):
                UnoController.total_cards = _total_cards
            punlish_card = UnoController.total_cards.popleft()
            punlish_cards.append(punlish_card)
        # Todo
        # Send the cards to the player
        pass

    def POST(self):
        pass


'''
class StandardCard(object):
    """
    Standard card, only for the number card
    """
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __str__(self):
        return self.color + "-" + str(self.number)

def initize_cards():
    """
    Initize the uno cards, each color have one zero card;
    each color have two cards(1-9)
    """
    cards = []
    for i in range(10):
        for color in ['b', 'g', 'r', 'y']:
            if i == 0:
                card = StandardCard(color, i)
                cards.append(card)
            else:
                card = StandardCard(color, i)
                cards.append(card)
                cards.append(card)
    return cards

def shuffle_cards(cards):
    return random.sample(cards, len(cards))
'''




def main():
    pass

if __name__ == '__main__':
    main()
