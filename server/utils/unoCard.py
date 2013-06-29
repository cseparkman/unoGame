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


def main():
    pass

if __name__ == '__main__':
    main()