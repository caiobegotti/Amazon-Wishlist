#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

import sys
import os.path
import optparse
import locale

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from amazonwishlist import wishlist
from amazonwishlist import profile
from amazonwishlist import config

def main():
    available = "store domains are %s" % (config.available())
    parser = optparse.OptionParser("Usage: %prog [options]")
    parser.add_option("-i", "--id", dest="userid", type="string", help="wishlist ID (i.e. 3MCYFXCFDH4FA)")
    parser.add_option("-s", "--store", dest="store", type="string", help=available)

    (options, args) = parser.parse_args()
    if options.userid is None:
        print 'At least the wishlist ID is necessary, store will default to the US one'
        parser.print_help()
    else:
        app(options.userid, options.store)


def app(userid, store):
    data = wishlist.Query(userid, country=store)

    print 'Authors or manufacturers:'
    for entry in data.authors():
        print '\t=' + entry

    print 'Items titles:'
    for entry in data.titles():
        print '\t=' + entry

    print 'Items covers:'
    for entry in data.covers():
        print '\t=' + entry

    print 'Items URLs:'
    for entry in data.urls():
        print '\t=' + entry

    print 'Items prices:'
    for entry in data.prices():
        print '\t=' + entry

    print 'Universal wishlist sources:'
    for entry in data.via():
        print '\t=' + entry

    print 'Ideas you saved for later:'
    for entry in data.ideas():
        print '\t=' + entry

    if 'EUR' in data.currency or 'BRL' in data.currency:
        locale.setlocale(locale.LC_MONETARY, 'de_DE.UTF-8')
    else:
        locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')

    print 'In %s your wishlist is worth %s%s' % (data.currency,
                                                 data.symbol,
                                                 locale.currency(data.total_expenses(),
                                                                 grouping=True,
                                                                 symbol=False))

    data = profile.Query(userid, country=store)

    print 'Your name and avatar:'
    print data.basic_info()

    print 'Your lists data:'
    print data.wishlists()

    print 'Your lists and their sizes:'
    print data.wishlists_details()

if __name__ == "__main__":
    main()
