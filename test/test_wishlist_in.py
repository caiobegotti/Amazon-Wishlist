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


class TestWishlistIndia:

    def setup_method(self, method):
        global wishlist
        wishlist = Wishlist('ZVKVJQHOBAT2', country='in')

    def test_prices(self):
        prices = wishlist.prices()
        for price in prices:
            try:
                float(price)
            except:
                if not '' in price and price is None:
                    assert price

    def test_urls(self):
        urls = wishlist.urls()
        assert is_match_for(DP, urls[0]) == True
        assert is_match_for(DP, urls[1]) == True
        assert is_match_for(DP, urls[2]) == True
        assert is_match_for(DP, urls[3]) == True

    def test_currency(self):
        assert wishlist.currency == 'INR'
        assert wishlist.symbol == ur'\u20B9'

    def test_covers(self):
        covers = wishlist.covers()
        assert is_match_for(URL, covers[0]) == True
        assert is_match_for(URL, covers[1]) == True
        assert is_match_for(URL, covers[2]) == True
        assert is_match_for(URL, covers[3]) == True

    def test_titles(self):
        titles = wishlist.titles()
        assert is_match_for(TITLE, titles[0]) == True
        assert is_match_for(TITLE, titles[1]) == True
        assert is_match_for(TITLE, titles[2]) == True
        assert is_match_for(TITLE, titles[3]) == True

    def test_authors(self):
        authors = wishlist.authors()
        assert is_match_for(TITLE, authors[0]) == True
        assert is_match_for(TITLE, authors[1]) == True
        assert is_match_for(TITLE, authors[2]) == True
        assert is_match_for(TITLE, authors[3]) == True
