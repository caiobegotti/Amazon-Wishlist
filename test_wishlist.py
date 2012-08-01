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

    def test_via(self):
        via = wl.via()
        assert via[-1] == 'xkcd.com'
        assert via[-2] == 'submarino.com.br'
        assert via[-3] == 'saraivauni.com.br'

    def test_urls(self):
        urls = wl.urls()
        assert urls[-5] == 'http://www.amazon.com/dp/1405116927'
        assert urls[-20] == 'http://www.amazon.com/dp/0631232702'
        assert urls[-40] == ''
        assert urls[5] == ''

    def test_currency(self):
        currency = wl.currency
        symbol = wl.symbol
        assert currency == 'USD'
        assert symbol == '$'

    def test_total(self):
        total = wl.total_expenses()
        assert str(total) == '7650.41'

    def test_covers(self):
        covers = wl.covers()
        assert covers[-1] == 'http://ecx.images-amazon.com/images/I/51o69JlFGQL._SL110_SL44_.jpg'
        assert covers[-4] == 'http://ecx.images-amazon.com/images/I/71SH2KAXPHL._SL110_PIsitb-sticker-arrow-sm,TopRight,10,-13_OU01_SL44_.gif'
        assert covers[-217] == 'http://g-ecx.images-amazon.com/images/G/01/gifts/registries/wishlist/note01._SX44_V135173731_.png'
        assert covers[-52] == 'http://g-ecx.images-amazon.com/images/G/01/x-locale/detail/thumb-no-image._SX44_V192211878_.gif'

   # titles = wl.titles()
   # authors = wl.authors()
