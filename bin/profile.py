#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import optparse

from amazonwish.amazonwish import Wishlist
from amazonwish.amazonwish import Profile

def basin():
    parser = optparse.OptionParser("Usage: %prog [options]")
    parser.add_option("-i", "--id", dest="id", type="string", help="wishlist ID (i.e. 3MCYFXCFDH4FA)")
    parser.add_option("-s", "--store", dest="store", type="string", help="store domain [us, uk, ca, fr, es, it, de, jp, cn, br, mx, in]")

    (options, args) = parser.parse_args()
    if options.id is None:
        print 'At least the wishlist ID is necessary, store will default to the US one'
        parser.print_help()
    else:
        tests(options.id, options.store)

def tests(id, store):
    if store is None:
        store = 'us'

    wl = Wishlist(id, country=store)

    print 'Authors or manufacturers:'
    authors = wl.authors()
    for entry in authors:
        print '\t=' + entry

    print 'Items titles:'
    titles = wl.titles()
    for entry in titles:
        print '\t=' + entry

    print 'Items covers:'
    covers = wl.covers()
    for entry in covers:
        print '\t=' + entry

    print 'Items URLs:'
    urls = wl.urls()
    for entry in urls:
        print '\t=' + entry

    print 'Items prices:'
    prices = wl.prices()
    for entry in prices:
        print '\t=' + entry
        #for c in entry:
        #    print '[%s]' % c, repr(c), type(c)

    print 'Universal wishlist sources:'
    via = wl.via()
    for entry in via:
        print '\t=' + entry

    ideas = wl.ideas()
    print 'Ideas you saved for later:'
    print ideas

    total = wl.total_expenses()
    print 'In %s your wishlist is worth %s%s' % (wl.currency, wl.symbol, total)
    
    p = Profile(id, country=store)

    info = p.basic_info()
    print 'Your name and avatar:'
    print info

    lists = p.wishlists()
    print 'Your lists data:'
    print lists

    details = p.wishlists_details()
    print 'Your lists and their sizes:'
    print details

if __name__ == "__main__":
    basin()
