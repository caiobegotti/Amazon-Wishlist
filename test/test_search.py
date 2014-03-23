#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

import sys
import os.path

# generic test helpers
from test_utils_functions import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from amazonwishlist import search


class TestSearchUS:

    def test_search(self):
        res = search.Query('caio1982@gmail.com', country='us')
        matches = res.list()[0]
        assert is_match_for(NAME, matches[0]) == True
        assert is_match_for(WISHLIST, matches[1]) == True


class TestSearchCanada:

    def test_search(self):
        res = search.Query('caio1982@gmail.com', country='ca')
        matches = res.list()[0]
        assert is_match_for(NAME, matches[0]) == True
        assert is_match_for(WISHLIST, matches[1]) == True


class TestSearchUK:

    def test_search(self):
        res = search.Query('caio1982@gmail.com', country='uk')
        matches = res.list()[0]
        assert is_match_for(NAME, matches[0]) == True
        assert is_match_for(WISHLIST, matches[1]) == True


class TestSearchGermany:

    def test_search(self):
        res = search.Query('caio1982@gmail.com', country='de')
        matches = res.list()[0]
        assert is_match_for(NAME, matches[0]) == True
        assert is_match_for(WISHLIST, matches[1]) == True


class TestSearchItaly:

    def test_search(self):
        res = search.Query('caio1982@gmail.com', country='it')
        matches = res.list()[0]
        assert is_match_for(NAME, matches[0]) == True
        assert is_match_for(WISHLIST, matches[1]) == True


class TestSearchFrance:

    def test_search(self):
        res = search.Query('caio1982@gmail.com', country='fr')
        matches = res.list()[0]
        assert is_match_for(NAME, matches[0]) == True
        assert is_match_for(WISHLIST, matches[1]) == True


class TestSearchSpain:

    def test_search(self):
        res = search.Query('caio1982@gmail.com', country='es')
        matches = res.list()[0]
        assert is_match_for(NAME, matches[0]) == True
        assert is_match_for(WISHLIST, matches[1]) == True


class TestSearchJapan:

    def test_search(self):
        res = search.Query('caio1982@gmail.com', country='jp')
        matches = res.list()[0]
        assert is_match_for(NAME, matches[0]) == True
        assert is_match_for(WISHLIST, matches[1]) == True


class TestSearchChina:

    def test_search(self):
        res = search.Query('caio1982@gmail.com', country='cn')
        matches = res.list()[0]
        assert is_match_for(NAME, matches[0]) == True
        assert is_match_for(WISHLIST, matches[1]) == True


class TestSearchIndia:

    def test_search(self):
        res = search.Query('caio1982@gmail.com', country='in')
        matches = res.list()[0]
        assert is_match_for(NAME, matches[0]) == True
        assert is_match_for(WISHLIST, matches[1]) == True


class TestSearchBrazil:

   def test_search(self):
       res = search.Query('caio1982@gmail.com', country='br')
       matches = res.list()[0]
       assert is_match_for(NAME, matches[0]) == True
       assert is_match_for(WISHLIST, matches[1]) == True


# class TestSearchMexico:
#    def test_search(self):
#        res = search.Query('caio1982@gmail.com', country='mx')
#        matches = res.list()[0]
#        assert is_match_for(NAME, matches[0]) == True
#        assert is_match_for(WISHLIST, matches[1]) == True
