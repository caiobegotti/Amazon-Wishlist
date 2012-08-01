#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

from amazonwish.config import *
from amazonwish.amazonwish import Profile

class TestUnitedStates:
    def setup_method(self, method):
        global p
        p = Profile('3MCYFXCFDH4FA', country='us')

    def test_basicInfo(self):
        info = p.basicInfo()
        assert info[0] == 'Caio Begotti'
        assert info[1] == 'http://ecx.images-amazon.com/images/I/71jwclpxTDL._SS150_.jpg'

    def test_wishlists(self):
        lists = p.wishlists()
        assert lists[0] == 'Stuff'
        assert lists[1] == 'Test'
        assert lists[2] == 'Wish List'

    def test_wishlistsDetails(self):
        details = p.wishlistsDetails()
        codes = details[0]
        sizes = details[1]
        assert codes[0] == '22LLDFNTWM5J7'
        assert codes[1] == '3K7YA6YZVXG9J'
        assert codes[2] == '3MCYFXCFDH4FA'
        assert sizes[0] == '4'
        assert sizes[1] == '1'
        assert sizes[2] == '217'

class TestUnitedKingdom:
    def setup_method(self, method):
        global p
        p = Profile('25LUEB8ZTW0YD', country='uk')

    def test_basicInfo(self):
        info = p.basicInfo()
        assert info[0] == 'Tony Mogg'

    def test_wishlists(self):
        lists = p.wishlists()
        assert lists[0] == 'Wish List'

    def test_wishlistsDetails(self):
        details = p.wishlistsDetails()
        codes = details[0]
        sizes = details[1]
        assert codes[0] == '25LUEB8ZTW0YD'
        assert sizes[0] == '24'

class TestJapan:
    def setup_method(self, method):
        global p
        p = Profile('2KRQL6OB16TTG', country='jp')

    def test_basicInfo(self):
        info = p.basicInfo()
        assert info[0] == 'Takeshi Kato'

    def test_wishlists(self):
        lists = p.wishlists()
        assert lists[0] == 'Wishlist'

    def test_wishlistsDetails(self):
        details = p.wishlistsDetails()
        codes = details[0]
        sizes = details[1]
        assert codes[0] == '2KRQL6OB16TTG'
        assert sizes[0] == '46'

class TestChina:
    def setup_method(self, method):
        global p
        p = Profile('3BNMGCLGH93KY', country='cn')

    def test_basicInfo(self):
        info = p.basicInfo()
        assert info[0] == 'ming'

    def test_wishlists(self):
        lists = p.wishlists()
        assert lists[0] == u'\u5fc3\u613f\u5355'

    def test_wishlistsDetails(self):
        details = p.wishlistsDetails()
        codes = details[0]
        sizes = details[1]
        assert codes[0] == '3BNMGCLGH93KY'
        assert sizes[0] == '198'

class TestFrance:
    def setup_method(self, method):
        global p
        p = Profile('377PE49C4Y7UC', country='fr')

    def test_basicInfo(self):
        info = p.basicInfo()
        assert info[0] == 'Olivier Blin'

    def test_wishlists(self):
        lists = p.wishlists()
        assert lists[0] == 'cadeaux'

    def test_wishlistsDetails(self):
        details = p.wishlistsDetails()
        codes = details[0]
        sizes = details[1]
        assert codes[0] == '377PE49C4Y7UC'
        assert sizes[0] == '18'

class TestCanada:
    def setup_method(self, method):
        global p
        p = Profile('2OO8G9NM4QYQJ', country='ca')

    def test_basicInfo(self):
        info = p.basicInfo()
        assert info[0] == 'Renata Rocha'

    def test_wishlists(self):
        lists = p.wishlists()
        assert lists[0] == 'Wish List'

    def test_wishlistsDetails(self):
        details = p.wishlistsDetails()
        codes = details[0]
        sizes = details[1]
        assert codes[0] == '2OO8G9NM4QYQJ'
        assert sizes[0] == '10'

class TestGermany:
    def setup_method(self, method):
        global p
        p = Profile('1JZ9TLZEUZHZX', country='de')

    def test_basicInfo(self):
        info = p.basicInfo()
        assert info[0] == 'Christian Zuck'

    def test_wishlists(self):
        lists = p.wishlists()
        assert lists[0] == 'Wunschzettel'

    def test_wishlistsDetails(self):
        details = p.wishlistsDetails()
        codes = details[0]
        sizes = details[1]
        assert codes[0] == '1JZ9TLZEUZHZX'
        assert sizes[0] == '240'

class TestItaly:
    def setup_method(self, method):
        global p
        p = Profile('Y0P9HTJILVLW', country='it')

    def test_basicInfo(self):
        info = p.basicInfo()
        assert info[0] == 'Luigi'

    def test_wishlists(self):
        lists = p.wishlists()
        assert lists[0] == 'Lista Desideri'

    def test_wishlistsDetails(self):
        details = p.wishlistsDetails()
        codes = details[0]
        sizes = details[1]
        assert codes[0] == 'Y0P9HTJILVLW'
        assert sizes[0] == '26'

class TestSpain:
    def setup_method(self, method):
        global p
        p = Profile('58GCAE5DT41X', country='es')

    def test_basicInfo(self):
        info = p.basicInfo()
        assert info[0] == 'Juan'

    def test_wishlists(self):
        lists = p.wishlists()
        assert lists[0] == 'Lista de deseos'

    def test_wishlistsDetails(self):
        details = p.wishlistsDetails()
        codes = details[0]
        sizes = details[1]
        assert codes[0] == '58GCAE5DT41X'
        assert sizes[0] == '16'
