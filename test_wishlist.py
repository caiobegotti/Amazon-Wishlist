#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

from amazonwish.config import *
from amazonwish.amazonwish import Wishlist

class TestWishlistUnitedStates:
    def setup_method(self, method):
        global wl
        wl = Wishlist('3MCYFXCFDH4FA', country='us')

    def test_ideas(self):
        ideas = wl.ideas()
        assert ideas[0] == u'Backpac\u200bk & trave\u200bl stuff'

    def test_prices(self):
        prices = wl.prices()
        assert prices[-5] == '74.95'
        assert prices[-9] == '119.95'
        assert prices[-15] == '7.99'
        assert prices[-59] == '32'
        assert prices[-217] == 'Idea'

   # titles = wl.titles()
   # authors = wl.authors()
   # covers = wl.covers()
   # urls = wl.urls()
   # via = wl.via()
