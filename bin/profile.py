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


def app():
    parser = optparse.OptionParser("Usage: %prog [options]")
    parser.add_option("-i", "--id", dest="userid", type="string", help="wishlist ID (i.e. 3MCYFXCFDH4FA)")
    parser.add_option("-s", "--store", dest="store", type="string", help="store domain [us, uk, ca, fr, es, it, de, jp, cn, br, mx, in]")

    (options, args) = parser.parse_args()
    if options.userid is None:
        print 'At least the wishlist ID is necessary, store will default to the US one'
        parser.print_help()
    else:
        retrieve(options.userid, options.store)


def retrieve(userid, store):
    wishlist = Wishlist(userid, country=store)

    print 'Authors or manufacturers:'
    authors = wishlist.authors()
    for entry in authors:
        print '\t=' + entry

    print 'Items titles:'
    titles = wishlist.titles()
    for entry in titles:
        print '\t=' + entry

    print 'Items covers:'
    covers = wishlist.covers()
    for entry in covers:
        print '\t=' + entry

    print 'Items URLs:'
    urls = wishlist.urls()
    for entry in urls:
        print '\t=' + entry

    print 'Items prices:'
    prices = wishlist.prices()
    for entry in prices:
        print '\t=' + entry

    print 'Universal wishlist sources:'
    via = wishlist.via()
    for entry in via:
        print '\t=' + entry

    ideas = wishlist.ideas()
    print 'Ideas you saved for later:'
    for entry in ideas:
        print '\t=' + entry

    total = wishlist.total_expenses()
    print 'In %s your wishlist is worth %s%s' % (wishlist.currency, wishlist.symbol, total)

    profile = Profile(userid, country=store)

    info = profile.basic_info()
    print 'Your name and avatar:'
    print info

    lists = profile.wishlists()
    print 'Your lists data:'
    print lists

    details = profile.wishlists_details()
    print 'Your lists and their sizes:'
    print details

if __name__ == "__main__":
    app()
