#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

import optparse

from amazonwish.config import *
from amazonwish.amazonwish import Wishlist
from amazonwish.amazonwish import Profile

def basin():
    parser = optparse.OptionParser("Usage: %prog [options]")
    parser.add_option("-i", "--id", dest="id", type="string", help="wishlist ID (i.e. 3MCYFXCFDH4FA)")
    parser.add_option("-s", "--store", dest="store", type="string", help="store domain [us, uk, ca, fr, es, it, de, jp, cn, br]")

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
    urls = wl.urls()
    prices = wl.prices()
    via = wl.via()
    ideas = wl.ideas()

    print 'The titles authors are:'
    for entry in authors:
        print '\t=' + entry

    print 'Your titles are:'
    for entry in titles:
        print '\t=' + entry

    print 'Your items covers:'
    for entry in covers:
        print '\t=' + entry

    print 'Items URLs are:'
    for entry in urls:
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

    lists = p.wishlists()
    print 'Your lists are:'
    print lists

    details = p.wishlistsDetails()
    print 'Your lists and their sizes:'
    print details

    total = wl.total_expenses()
    print 'Your wishlist is worth ' + wl.currency + ' ' + wl.symbol + str(total)

    #print zip(titles, prices)

    #print 'Vias: ' + str(len(via))
    #print 'Authors: ' + str(len(authors))
    #print 'Titles: ' + str(len(titles))
    #print 'Prices: ' + str(len(prices))
    #print 'URLs: ' + str(len(urls))
    #print 'Covers: ' + str(len(covers))

    ideas = wl.ideas()
    print ideas

if __name__ == "__main__":
    basin()
