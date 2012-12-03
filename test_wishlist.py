#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

from amazonwish.config import *
from amazonwish.amazonwish import Wishlist

class TestWishlistUS:
    def setup_method(self, method):
        global wl
        wl = Wishlist('3MCYFXCFDH4FA', country='us')

    def test_ideas(self):
        ideas = wl.ideas()
        assert ideas[0] == 'Backpack & travel stuff'

    def test_prices(self):
        prices = wl.prices()
        for p in prices:
            try:
                float(p)
            except:
                if not 'Idea' in p and p is None:
                    assert p

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

    def test_currency(self):
        currency = wl.currency
        symbol = wl.symbol
        assert currency == 'USD'
        assert symbol == '$'

    def test_covers(self):
        covers = wl.covers()
        assert covers[6] == 'http://g-ecx.images-amazon.com/images/G/01/gifts/registries/wishlist/note01.png'
        assert covers[219] == 'http://ecx.images-amazon.com/images/I/71SH2KAXPHL.gif'
        assert covers[171] == 'http://g-ecx.images-amazon.com/images/G/01/x-locale/detail/thumb-no-image.gif'
        assert covers[181] == 'http://ecx.images-amazon.com/images/I/019%2BQ0fbhrL.jpg'

    def test_titles(self):
        titles = wl.titles()
        assert titles[-5] == 'The Handbook of Language Variation and Change (Blackwell Handbooks in Linguistics)'
        assert titles[-7] == 'The World\'s Major Languages'
        assert titles[-9] == 'Three is a Crowd?: Acquiring Portuguese in a Trilingual Environment (Child Language and Child Development)'
        assert titles[-10] == 'Computational Processing of the Portuguese Language: 7th International Workshop, PROPOR 2006, Itatiaia, Brazil, May 13-17, 2006, Proceedings (Lecture ... / Lecture Notes in Artificial Intelligence)'
        assert titles[-13] == u'The Posthumous Memoirs of Brás Cubas (Library of Latin America)'
        assert titles[-35] == 'Dilbert 2.0: 20 Years of Dilbert'
        assert titles[-43] == 'A Ditadura Encurralada'
        #assert unicode(titles[-50]) == u'As Cem Melhores Cr\u0244nicas Brasileiras'
        assert titles[-53] == 'Punk'
        #assert titles[-67] == 'Law \& Order: Crime Scenes'

    def test_authors(self):
        authors = wl.authors()
        assert authors[-1] == 'Paul Brians (Author)'
        assert authors[-5] == 'J. K. Chambers (Editor), et al.'
        assert authors[-6] == 'Walt Wolfram'
        assert authors[-17] == 'Rosina Lippi-Green'
        assert authors[-30] == 'Frans De Waal, F. B. M. De Waal'
        assert authors[-45] == ''
