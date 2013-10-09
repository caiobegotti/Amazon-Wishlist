#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from amazonwish.amazonwish import Wishlist


class TestWishlistUS:

    def setup_method(self, method):
        global wishlist
        wishlist = Wishlist('3MCYFXCFDH4FA', country='us')

    def test_ideas(self):
        ideas = wishlist.ideas()
        assert ideas[0] == 'Backpack & travel stuff'

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
        assert via[-1] == 'xkcd.com'
        assert via[-2] == 'submarino.com.br'
        assert via[-3] == 'saraivauni.com.br'

    def test_urls(self):
        urls = wishlist.urls()
        assert urls[-5] == 'http://www.amazon.com/dp/1405116927'
        assert urls[-20] == 'http://www.amazon.com/dp/0631232702'
        assert urls[-40] == ''

    def test_currency(self):
        currency = wishlist.currency
        symbol = wishlist.symbol
        assert currency == 'USD'
        assert symbol == '$'

    def test_covers(self):
        covers = wishlist.covers()
        assert covers[6] == 'http://g-ecx.images-amazon.com/images/G/01/gifts/registries/wishlist/note01.png'
        assert covers[219] == 'http://ecx.images-amazon.com/images/I/71SH2KAXPHL.gif'
        assert covers[171] == 'http://g-ecx.images-amazon.com/images/G/01/x-locale/detail/thumb-no-image.gif'
        assert covers[181] == 'http://ecx.images-amazon.com/images/I/019%2BQ0fbhrL.jpg'

    def test_titles(self):
        titles = wishlist.titles()
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
        authors = wishlist.authors()
        assert authors[-1] == 'Paul Brians (Author)'
        assert authors[-5] == 'J. K. Chambers (Editor), et al.'
        assert authors[-6] == 'Walt Wolfram'
        assert authors[-17] == 'Rosina Lippi-Green'
        assert authors[-30] == 'Frans De Waal, F. B. M. De Waal'
        assert authors[-45] == ''


class TestWishlistUK:

    def setup_method(self, method):
        global wishlist
        wishlist = Wishlist('MBI8TEEYJS10', country='uk')

    def test_prices(self):
        prices = wishlist.prices()
        for price in prices:
            try:
                float(price)
            except:
                if not 'Idea' in price and price is None:
                    assert price

    def test_urls(self):
        urls = wishlist.urls()
        assert urls[0] == 'http://www.amazon.co.uk/dp/B005890FUI'
        assert urls[1] == 'http://www.amazon.co.uk/dp/B008ETX1C8'
        assert urls[2] == 'http://www.amazon.co.uk/dp/B005UYF6DW'
        assert urls[3] == 'http://www.amazon.co.uk/dp/B003R0KOUQ'

    def test_currency(self):
        currency = wishlist.currency
        symbol = wishlist.symbol
        assert currency == 'GBP'
        assert symbol == ur'\u00a3'

    def test_covers(self):
        covers = wishlist.covers()
        assert covers[0] == 'http://ecx.images-amazon.com/images/I/41JpsttW8CL.jpg'
        assert covers[1] == 'http://ecx.images-amazon.com/images/I/41witgYTdsL.jpg'
        assert covers[2] == 'http://ecx.images-amazon.com/images/I/311M2ljl9kL.jpg'
        assert covers[3] == 'http://ecx.images-amazon.com/images/I/514nO64FYTL.jpg'

    def test_titles(self):
        titles = wishlist.titles()
        assert titles[0] == 'Kindle Touch, Wi-Fi, 6" E Ink Touch Screen Display'
        assert titles[1] == 'Official Team GB Cycling Duck'
        assert titles[2] == "Rockport Men's Charlesview Black Lace Up K71053  12.5 UK, 13 US"
        assert titles[3] == 'Avatar with Limited Edition Lenticular Artwork (Blu-ray 3D + Blu-ray + DVD)[Region Free]'

    def test_authors(self):
        authors = wishlist.authors()
        assert authors[0] == ''
        assert authors[1] == ''
        assert authors[2] == ''
        assert authors[3] == 'Sam Worthington'


class TestWishlistFrance:

    def setup_method(self, method):
        global wishlist
        wishlist = Wishlist('2POKVB3027QIK', country='fr')

    def test_prices(self):
        prices = wishlist.prices()
        for price in prices:
            try:
                float(price)
            except:
                if not 'Idea' in price and price is None:
                    assert price

    def test_urls(self):
        urls = wishlist.urls()
        assert urls[0] == 'http://www.amazon.fr/dp/B008384GHE'
        assert urls[1] == 'http://www.amazon.fr/dp/2350761231'
        assert urls[2] == 'http://www.amazon.fr/dp/2315002885'
        assert urls[3] == 'http://www.amazon.fr/dp/2020537966'

    def test_currency(self):
        currency = wishlist.currency
        symbol = wishlist.symbol
        assert currency == 'EUR'
        assert symbol == ur'\u20ac'

    def test_covers(self):
        covers = wishlist.covers()
        assert covers[0] == 'http://ecx.images-amazon.com/images/I/51rKu1rvV8L.jpg'
        assert covers[1] == 'http://ecx.images-amazon.com/images/I/41FcoyEUXBL.jpg'
        assert covers[2] == 'http://ecx.images-amazon.com/images/I/513-V9oAo0L.jpg'
        assert covers[3] == 'http://ecx.images-amazon.com/images/I/51WKWFVF81L.jpg'

    def test_titles(self):
        titles = wishlist.titles()
        assert titles[0] == u'Les dents de la mer - Bo\xeetier m\xe9tal [Blu-ray]'
        assert titles[1] == "L'Agenda VDM 2012-2013"
        assert titles[2] == "Shakespeare, c'est moi: La confession d'Edward de Vere"
        assert titles[3] == u"Moi j'adore, la ma\xeetresse d\xe9teste"

    def test_authors(self):
        authors = wishlist.authors()
        assert authors[0] == ''
        assert authors[1] == 'Roy Scheider'
        assert authors[2] == 'Didier Guedj (Auteur), et al.'
        assert authors[3] == u'Jouannic Br\xfcnhilde (Auteur)'
        assert authors[4] == u'Elisabeth Brami (Auteur), Lionel Le N\xe9ouanic (Illustrations)'
