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





def main():
    pass

if __name__ == '__main__':
    main()
