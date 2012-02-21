#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import exit

from lib.config import Config
from lib.amazonwish import Wishlist
from lib.amazonwish import Profile

from lxml.html import tostring

class Main:
    def __init__(self):
        country = 'us'
        wl = Wishlist()
        params = wl.readConfig(country)
        page = wl.downloadPage(params,'3MCYFXCFDH4FA')

        titles = wl.titles(page)
        authors = wl.authors(page)
        covers = wl.covers(page)
        prices = wl.prices(page)
        via = wl.via(page)

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

        p = Profile()
        params = p.readConfig(country)
        page = p.downloadPage(params,'3MCYFXCFDH4FA')

        info = p.basicInfo(page)
        print 'Your name and avatar:'
        print info

        lists = p.wishlistsDetails(page)
        print 'Your lists and their sizes:'
        print lists

if __name__ == "__main__":
    Main()
