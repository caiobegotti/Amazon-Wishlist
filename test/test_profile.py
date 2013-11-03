#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

import sys
import os.path

# generic test helpers
from test_utils_functions import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from amazonwishlist import profile

class TestUS:

    def setup_method(self, method):
        global person
        person = profile.Query('3MCYFXCFDH4FA', country='us')

    def test_basic_info(self):
        info = person.basic_info()
        assert is_match_for(NAME, info[0]) == True
        assert is_match_for(URL, info[1]) == True

    def test_wishlists(self):
        lists = person.wishlists()
        assert is_match_for(NAME, lists[0]) == True
        assert is_match_for(NAME, lists[1]) == True
        assert is_match_for(NAME, lists[2]) == True

    def test_wishlists_details(self):
        details = person.wishlists_details()
        codes = details[0]
        sizes = details[1]
        assert is_match_for(WISHLIST, codes[0]) == True
        assert is_match_for(WISHLIST, codes[1]) == True
        assert is_match_for(WISHLIST, codes[2]) == True
        assert is_match_for(NUMBER, sizes[0]) == True
        assert is_match_for(NUMBER, sizes[1]) == True
        assert is_match_for(NUMBER, sizes[2]) == True


class TestUK:

    def setup_method(self, method):
        global person
        person = profile.Query('MBI8TEEYJS10', country='uk')

    def test_basic_info(self):
        info = person.basic_info()
        assert is_match_for(NAME, info[0]) == True
        assert is_match_for(URL, info[1]) == True

    def test_wishlists(self):
        lists = person.wishlists()
        assert is_match_for(NAME, lists[0]) == True

    def test_wishlists_details(self):
        details = person.wishlists_details()
        codes = details[0]
        sizes = details[1]
        assert is_match_for(WISHLIST, codes[0]) == True
        assert is_match_for(NUMBER, sizes[0]) == True


class TestJapan:

    def setup_method(self, method):
        global person
        person = profile.Query('13RB1XNS2VF62', country='jp')

    def test_basic_info(self):
        info = person.basic_info()
        assert is_match_for(NAME, info[0]) == True
        assert is_match_for(URL, info[1]) == True

    def test_wishlists(self):
        lists = person.wishlists()
        assert lists[0] == u'\u65b0\u3057\u3044\u307b\u3057\u3044\u7269\u200b\u30ea\u30b9\u30c8'

    def test_wishlists_details(self):
        details = person.wishlists_details()
        codes = details[0]
        sizes = details[1]
        assert is_match_for(WISHLIST, codes[0]) == True
        assert is_match_for(NUMBER, sizes[0]) == True


class TestChina:

    def setup_method(self, method):
        global person
        person = profile.Query('3BFG9M3CL83QR', country='cn')

    def test_basic_info(self):
        info = person.basic_info()
        assert is_match_for(NAME, info[0]) == True
        assert is_match_for(URL, info[1]) == True

    def test_wishlists(self):
        lists = person.wishlists()
        assert lists[0] == u'\u5fc3\u613f\u5355'

    def test_wishlists_details(self):
        details = person.wishlists_details()
        codes = details[0]
        sizes = details[1]
        assert is_match_for(WISHLIST, codes[0]) == True
        assert is_match_for(NUMBER, sizes[0]) == True


class TestFrance:

    def setup_method(self, method):
        global person
        person = profile.Query('2POKVB3027QIK', country='fr')

    def test_basic_info(self):
        info = person.basic_info()
        assert is_match_for(NAME, info[0]) == True
        assert is_match_for(URL, info[1]) == True

    def test_wishlists(self):
        lists = person.wishlists()
        assert is_match_for(NAME, lists[0]) == True

    def test_wishlists_details(self):
        details = person.wishlists_details()
        codes = details[0]
        sizes = details[1]
        assert is_match_for(WISHLIST, codes[0]) == True
        assert is_match_for(NUMBER, sizes[0]) == True


class TestCanada:

    def setup_method(self, method):
        global person
        person = profile.Query('PEK9J1M112UK', country='ca')

    def test_basic_info(self):
        info = person.basic_info()
        assert is_match_for(NAME, info[0]) == True
        assert is_match_for(URL, info[1]) == True

    def test_wishlists(self):
        lists = person.wishlists()
        assert is_match_for(NAME, lists[0]) == True

    def test_wishlists_details(self):
        details = person.wishlists_details()
        codes = details[0]
        sizes = details[1]
        assert is_match_for(WISHLIST, codes[0]) == True
        assert is_match_for(NUMBER, sizes[0]) == True


class TestGermany:

    def setup_method(self, method):
        global person
        person = profile.Query('2ZPN6SBGBP4X8', country='de')

    def test_basic_nfo(self):
        info = person.basic_info()
        assert is_match_for(NAME, info[0]) == True
        assert is_match_for(URL, info[1]) == True

    def test_wishlists(self):
        lists = person.wishlists()
        assert is_match_for(NAME, lists[0]) == True

    def test_wishlists_details(self):
        details = person.wishlists_details()
        codes = details[0]
        sizes = details[1]
        assert is_match_for(WISHLIST, codes[0]) == True
        assert is_match_for(NUMBER, sizes[0]) == True


class TestItaly:

    def setup_method(self, method):
        global person
        person = profile.Query('3W1RQNDJTCQC', country='it')

    def test_basic_info(self):
        info = person.basic_info()
        assert is_match_for(NAME, info[0]) == True
        assert is_match_for(URL, info[1]) == True

    def test_wishlists(self):
        lists = person.wishlists()
        assert is_match_for(NAME, lists[0]) == True

    def test_wishlists_details(self):
        details = person.wishlists_details()
        codes = details[0]
        sizes = details[1]
        assert is_match_for(WISHLIST, codes[0]) == True
        assert is_match_for(NUMBER, sizes[0]) == True


class TestSpain:

    def setup_method(self, method):
        global person
        person = profile.Query('1LJ10M7BWAICD', country='es')

    def test_basic_info(self):
        info = person.basic_info()
        assert is_match_for(NAME, info[0]) == True
        assert is_match_for(URL, info[1]) == True

    def test_wishlists(self):
        lists = person.wishlists()
        assert is_match_for(NAME, lists[0]) == True

    def test_wishlists_details(self):
        details = person.wishlists_details()
        codes = details[0]
        sizes = details[1]
        assert is_match_for(WISHLIST, codes[0]) == True
        assert is_match_for(NUMBER, sizes[0]) == True


# class TestBrazil:
#    def setup_method(self, method):
#        global person
#        person = Profile('', country='br')
#
#    def test_basic_info(self):
#        info = person.basic_info()
#        assert is_match_for(NAME, info[0]) == True
#        assert is_match_for(URL, info[1]) == True
#
#    def test_wishlists(self):
#        lists = person.wishlists()
#        assert is_match_for(NAME, lists[0]) == True
#
#    def test_wishlists_details(self):
#        details = person.wishlists_details()
#        codes = details[0]
#        sizes = details[1]
#        assert is_match_for(WISHLIST, codes[0]) == True
#        assert is_match_for(NUMBER, sizes[0]) == True
#
#
# class TestMexico:
#    def setup_method(self, method):
#        global person
#        person = Profile('', country='mx')
#
#    def test_basic_info(self):
#        info = person.basic_info()
#        assert is_match_for(NAME, info[0]) == True
#        assert is_match_for(URL, info[1]) == True
#
#    def test_wishlists(self):
#        lists = person.wishlists()
#        assert is_match_for(NAME, lists[0]) == True
#
#    def test_wishlists_details(self):
#        details = person.wishlists_details()
#        codes = details[0]
#        sizes = details[1]
#        assert is_match_for(WISHLIST, codes[0]) == True
#        assert is_match_for(NUMBER, sizes[0]) == True
