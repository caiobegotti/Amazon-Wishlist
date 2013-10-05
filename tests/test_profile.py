#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

from amazonwish.config import *
from amazonwish.amazonwish import Profile

class TestUS:
    def setup_method(self, method):
        global p
        p = Profile('3MCYFXCFDH4FA', country='us')

    def test_basicInfo(self):
        info = p.basicInfo()
        assert info[0] == 'Caio Begotti'
        assert info[1] == 'http://ecx.images-amazon.com/images/I/51-aMSvDbhL.jpg'

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
        assert sizes[0] == '10'
        assert sizes[1] == '1'
        assert sizes[2] >= '200'

class TestUK:
    def setup_method(self, method):
        global p
        p = Profile('MBI8TEEYJS10', country='uk')

    def test_basicInfo(self):
        info = p.basicInfo()
        assert info[0] == 'Caio Begotti'

    def test_wishlists(self):
        lists = p.wishlists()
        assert lists[0] == 'Wish List'

    def test_wishlistsDetails(self):
        details = p.wishlistsDetails()
        codes = details[0]
        sizes = details[1]
        assert codes[0] == 'MBI8TEEYJS10'
        assert sizes[0] == '4'

class TestJapan:
    def setup_method(self, method):
        global p
        p = Profile('13RB1XNS2VF62', country='jp')

    def test_basicInfo(self):
        info = p.basicInfo()
        assert info[0] == 'Caio Begotti'

    def test_wishlists(self):
        lists = p.wishlists()
        assert lists[0] == u'\u65b0\u3057\u3044\u307b\u3057\u3044\u7269\u200b\u30ea\u30b9\u30c8'

    def test_wishlistsDetails(self):
        details = p.wishlistsDetails()
        codes = details[0]
        sizes = details[1]
        assert codes[0] == '13RB1XNS2VF62'
        assert sizes[0] == '1'

class TestChina:
    def setup_method(self, method):
        global p
        p = Profile('3BFG9M3CL83QR', country='cn')

    def test_basicInfo(self):
        info = p.basicInfo()
        assert info[0] == 'Caio Begotti'

    def test_wishlists(self):
        lists = p.wishlists()
        assert lists[0] == u'\u5fc3\u613f\u5355'

    def test_wishlistsDetails(self):
        details = p.wishlistsDetails()
        codes = details[0]
        sizes = details[1]
        assert codes[0] == '3BFG9M3CL83QR'
        assert sizes[0] == '1'

class TestFrance:
    def setup_method(self, method):
        global p
        p = Profile('2POKVB3027QIK', country='fr')

    def test_basicInfo(self):
        info = p.basicInfo()
        assert info[0] == 'Caio Begotti'

    def test_wishlists(self):
        lists = p.wishlists()
        assert lists[0] == 'Wish FRANCE'

    def test_wishlistsDetails(self):
        details = p.wishlistsDetails()
        codes = details[0]
        sizes = details[1]
        assert codes[0] == '2POKVB3027QIK'
        assert sizes[0] == '4'

class TestCanada:
    def setup_method(self, method):
        global p
        p = Profile('PEK9J1M112UK', country='ca')

    def test_basicInfo(self):
        info = p.basicInfo()
        assert info[0] == 'Caio Begotti'

    def test_wishlists(self):
        lists = p.wishlists()
        assert lists[0] == 'Wish Canada'

    def test_wishlistsDetails(self):
        details = p.wishlistsDetails()
        codes = details[0]
        sizes = details[1]
        assert codes[0] == 'PEK9J1M112UK'
        assert sizes[0] == '2'

class TestGermany:
    def setup_method(self, method):
        global p
        p = Profile('2ZPN6SBGBP4X8', country='de')

    def test_basicInfo(self):
        info = p.basicInfo()
        assert info[0] == 'Caio Begotti'

    def test_wishlists(self):
        lists = p.wishlists()
        assert lists[0] == 'WL germany'

    def test_wishlistsDetails(self):
        details = p.wishlistsDetails()
        codes = details[0]
        sizes = details[1]
        assert codes[0] == '2ZPN6SBGBP4X8'
        assert sizes[0] == '3'

class TestItaly:
    def setup_method(self, method):
        global p
        p = Profile('3W1RQNDJTCQC', country='it')

    def test_basicInfo(self):
        info = p.basicInfo()
        assert info[0] == 'Caio Begotti'

    def test_wishlists(self):
        lists = p.wishlists()
        assert lists[0] == 'Desideri IT'

    def test_wishlistsDetails(self):
        details = p.wishlistsDetails()
        codes = details[0]
        sizes = details[1]
        assert codes[0] == '3W1RQNDJTCQC'
        assert sizes[0] == '4'

class TestSpain:
    def setup_method(self, method):
        global p
        p = Profile('1LJ10M7BWAICD', country='es')

    def test_basicInfo(self):
        info = p.basicInfo()
        assert info[0] == 'Caio Begotti'

    def test_wishlists(self):
        lists = p.wishlists()
        assert lists[0] == 'Lista de deseos'

    def test_wishlistsDetails(self):
        details = p.wishlistsDetails()
        codes = details[0]
        sizes = details[1]
        assert codes[0] == '1LJ10M7BWAICD'
        assert sizes[0] == '3'

#class TestBrazil:
#    def setup_method(self, method):
#        global p
#        p = Profile('', country='br')
#
#    def test_basicInfo(self):
#        info = p.basicInfo()
#        assert info[0] == 'Caio Begotti'
#
#    def test_wishlists(self):
#        lists = p.wishlists()
#        assert lists[0] == 'Lista de desejos'
#
#    def test_wishlistsDetails(self):
#        details = p.wishlistsDetails()
#        codes = details[0]
#        sizes = details[1]
#        assert codes[0] == ''
#        assert sizes[0] == ''
