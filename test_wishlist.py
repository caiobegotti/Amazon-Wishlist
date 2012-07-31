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
        ideas = wl.ideas()[0]
        assert ideas == u'Backpac\u200bk & trave\u200bl stuff'
   # titles = wl.titles()
   # authors = wl.authors()
   # covers = wl.covers()
   # urls = wl.urls()
   # prices = wl.prices()
   # via = wl.via()
   # ideas = wl.ideas()
