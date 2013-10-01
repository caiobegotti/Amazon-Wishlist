#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

import optparse

from amazonwish.amazonwish import Search

def search():
    parser = optparse.OptionParser("Usage: %prog [options]")
    parser.add_option("-q", "--query", dest="query", type="string", help="query someone's info (i.e. caio1982@gmail.com)")
    parser.add_option("-s", "--store", dest="store", type="string", help="store domain [us, uk, ca, fr, es, it, de, jp, cn, br]")

    (options, args) = parser.parse_args()
    if options.query is None:
        print 'You must input at least a valid query string, name or e-mail address, store will default to the main one'
        parser.print_help()
    else:
        tests(options.query, options.store)

def tests(query, store):
    if store is None:
        store = 'us'

    s = Search(query, country=store)
    matches = s.list()

    for m in matches:
        print m

if __name__ == "__main__":
    search()
