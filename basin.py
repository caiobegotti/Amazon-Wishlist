#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import exit

from amazonwish.config import *
from amazonwish.amazonwish import Wishlist
from amazonwish.amazonwish import Profile

from lxml.html import tostring

class Main:
    def __init__(self):
        wl = Wishlist('3BNMGCLGH93KY', country='cn')

        titles = wl.titles()
        authors = wl.authors()
        covers = wl.covers()
        prices = wl.prices()
        via = wl.via()

        print 'Your titles are:'
        for entry in titles: 
            print '\t' + entry

        print 'The titles authors are:'
        for entry in authors: 
            print '\t' + entry

        print 'Your items covers:'
        for entry in covers: 
            print '\t' + entry

        print 'Their prices:'
        for entry in prices:
            print '\t' + entry

        print 'Some external sources:'
        for entry in via: 
            print '\t' + entry

        p = Profile('3BNMGCLGH93KY', country='cn')

        info = p.basicInfo()
        print 'Your name and avatar:'
        print info

        lists = p.wishlistsDetails()
        print 'Your lists and their sizes:'
        print lists

        #total = wl.total_expenses()
        #print 'How much would you need to buy all these? ' + total

if __name__ == "__main__":
    Main()
