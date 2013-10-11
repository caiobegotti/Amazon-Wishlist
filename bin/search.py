#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import optparse

from amazonwishlist.search import Search
from amazonwishlist import config


def app():
    available = "store domains are %s" % (config.available())
    parser = optparse.OptionParser("Usage: %prog [options]")
    parser.add_option("-q", "--query", dest="query", type="string", help="query someone's info (i.e. friend@service.com)")
    parser.add_option("-s", "--store", dest="store", type="string", help=available)

    (options, args) = parser.parse_args()
    if options.query is None:
        print 'You must input at least a valid query string, name or e-mail address, store will default to the main one'
        parser.print_help()
    else:
        search(options.query, options.store)


def search(query, store):
    if store is None:
        store = 'us'
    res = Search(query, country=store)
    matches = res.list()

    for match in matches:
        print match

if __name__ == "__main__":
    app()
