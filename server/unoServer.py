# coding:utf-8
#-------------------------------------------------------------------------------
#
# Author:      parkman
#
# Created:     28-06-2013
# Copyright:   (c) parkman 2013
# Licence:     <MIT>
#-------------------------------------------------------------------------------
import web
import random

from unoController import UnoController
from utils.unoCard import StandardCard
from utils.functions import *

url = (
    '/uno/card/(.+)', 'UnoController'
)

app = web.application(urls, globals())

def main():
    pass

if __name__ == '__main__':
    main()
