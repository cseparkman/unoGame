# coding:utf-8
#-------------------------------------------------------------------------------
#
# Author:      parkman
#
# Created:     28-06-2013
# Copyright:   (c) parkman 2013
# Licence:     <MIT>
#-------------------------------------------------------------------------------
from collections import deque
from utils.unCard import StandardCard


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

def shuffle_cards():
    cards = initize_cards()
    _cards = random.sample(cards, len(cards))
    return deque(_cards)

cards = shuffle_cards()

def re_shuffle_cards(cards):
    return random.sample(cards, len(cards))

def main():
    pass

if __name__ == '__main__':
    main()
