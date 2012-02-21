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
        covers = wl.covers(page)
        authors = wl.authors(page)
        prices = wl.prices(page)
        via = wl.via(page)

        for entry in titles: 
            res = tostring(entry, encoding='utf-8', method='text', pretty_print=True).strip()
            print res

        p = Profile()
        params = p.readConfig(country)
        page = p.downloadPage(params,'3MCYFXCFDH4FA')

        lists = p.wishlists(page)

        for entry in lists:
            res = tostring(entry, encoding='utf-8', method='text', pretty_print=True).strip()
            print res

if __name__ == "__main__":
    Main()
