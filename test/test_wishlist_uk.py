#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

import sys
import os.path

# generic test helpers 
from test_utils_functions import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from amazonwishlist import wishlist


class TestWishlistUK:

    def setup_method(self, method):
        global res
        res = wishlist.Query('MBI8TEEYJS10', country='uk')

    def test_prices(self):
        prices = res.prices()
        for price in prices:
            try:
                float(price)
            except:
                if not 'Idea' in price and price is None:
                    assert price

    def test_urls(self):
        urls = res.urls()
        assert is_match_for(DP, urls[0]) == True
        assert is_match_for(DP, urls[1]) == True
        assert is_match_for(DP, urls[2]) == True
        assert is_match_for(DP, urls[3]) == True

    def test_currency(self):
        assert res.currency == 'GBP'
        assert res.symbol == ur'\u00a3'

    def test_covers(self):
        covers = res.covers()
        assert is_match_for(URL, covers[0]) == True
        assert is_match_for(URL, covers[1]) == True
        assert is_match_for(URL, covers[2]) == True
        assert is_match_for(URL, covers[3]) == True

    def test_titles(self):
        titles = res.titles()
        assert is_match_for(TITLE, titles[0]) == True
        assert is_match_for(TITLE, titles[1]) == True
        assert is_match_for(TITLE, titles[2]) == True
        assert is_match_for(TITLE, titles[3]) == True

    def test_authors(self):
        authors = res.authors()
        assert is_match_for(TITLE, authors[0]) == True
        assert is_match_for(TITLE, authors[1]) == True
        assert is_match_for(TITLE, authors[2]) == True
        assert is_match_for(TITLE, authors[3]) == True
