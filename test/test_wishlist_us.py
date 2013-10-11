#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

import sys
import os.path

# generic test helpers 
from test_utils_functions import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from amazonwishlist.wishlist import Wishlist


class TestWishlistUS:

    def setup_method(self, method):
        global wishlist
        wishlist = Wishlist('3MCYFXCFDH4FA', country='us')

    def test_ideas(self):
        ideas = wishlist.ideas()
        assert is_match_for(TITLE, ideas[0]) == True

    def test_prices(self):
        prices = wishlist.prices()
        for price in prices:
            try:
                float(price)
            except:
                if not 'Idea' in price and price is None:
                    assert price

    def test_via(self):
        via = wishlist.via()
        assert is_match_for(VIA, via[0]) == True
        assert is_match_for(VIA, via[1]) == True
        assert is_match_for(VIA, via[2]) == True

    def test_urls(self):
        urls = wishlist.urls()
        assert is_match_for(DP, urls[5]) == True
        assert is_match_for(DP, urls[25]) == True
        assert is_match_for(DP, urls[50]) == True

    def test_currency(self):
        assert wishlist.currency == 'USD'
        assert wishlist.symbol == ur'\u0024'

    def test_covers(self):
        covers = wishlist.covers()
        assert is_match_for(URL, covers[0]) == True
        assert is_match_for(URL, covers[55]) == True
        assert is_match_for(URL, covers[175]) == True
        assert is_match_for(URL, covers[200]) == True
        assert is_match_for(URL, covers[225]) == True

    def test_titles(self):
        titles = wishlist.titles()
        assert is_match_for(TITLE, titles[0]) == True
        assert is_match_for(TITLE, titles[5]) == True
        assert is_match_for(TITLE, titles[10]) == True
        assert is_match_for(TITLE, titles[35]) == True
        assert is_match_for(TITLE, titles[45]) == True
        assert is_match_for(TITLE, titles[95]) == True
        assert is_match_for(TITLE, titles[110]) == True
        assert is_match_for(TITLE, titles[140]) == True
        assert is_match_for(TITLE, titles[160]) == True
        assert is_match_for(TITLE, titles[200]) == True

    def test_authors(self):
        authors = wishlist.authors()
        assert is_match_for(TITLE, authors[0]) == True
        assert is_match_for(TITLE, authors[1]) == True
        assert is_match_for(TITLE, authors[5]) == True
        assert is_match_for(TITLE, authors[10]) == True
        assert is_match_for(TITLE, authors[45]) == True
