#!/usr/bin/env python
# -*- coding: utf-8 -*-

import optparse

from sys import exit

from amazonwish.config import *
from amazonwish.amazonwish import Wishlist
from amazonwish.amazonwish import Profile

def basin():
    parser = optparse.OptionParser("Usage: %prog [options]")
    parser.add_option("-i", "--id", dest="id", type="string", help="wishlist ID (i.e. 3MCYFXCFDH4FA)")
    parser.add_option("-s", "--store", dest="store", type="string", help="store domain (e.g. us, ca, uk)")
 
    (options, args) = parser.parse_args()
    if options.id is None:
        print 'At least the wishlist ID is necessary, store will default to the main one'
        parser.print_help()
    else:
        tests(options.id, options.store)

def tests(id, store):
    if store is None:
        store = 'us'

    wl = Wishlist(id, country=store)

    titles = wl.titles()
    authors = wl.authors()
    covers = wl.covers()
    prices = wl.prices()
    via = wl.via()

    print 'The titles authors are:'
    for entry in authors: 
        print '\t=' + entry

    print 'Your titles are:'
    for entry in titles: 
        print '\t=' + entry

    print 'Your items covers:'
    for entry in covers: 
        print '\t=' + entry
    
    print 'Their prices:'
    for entry in prices:
        print '\t=' + entry

    print 'Some external sources:'
    for entry in via: 
        print '\t=' + entry

    p = Profile(id, country=store)

    info = p.basicInfo()
    print 'Your name and avatar:'
    print info

    lists = p.wishlistsDetails()
    print 'Your lists and their sizes:'
    print lists

    total = wl.total_expenses()
    print 'Your wishlist is worth ' + wl.currency + ' ' + wl.symbol + str(total)

    #print zip(titles, prices)

if __name__ == "__main__":
    basin()
