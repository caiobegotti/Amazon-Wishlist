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


class TestSearchUSMultiple:

    def test_search(self):
        res = search.Query('begotti', country='us')
        matches = res.list()
        assert is_match_for(NAME, matches[0][0]) == True
        assert is_match_for(NAME, matches[1][0]) == True
        assert is_match_for(WISHLIST, matches[0][1]) == True
        assert is_match_for(WISHLIST, matches[1][1]) == True


class TestSearchCAMultiple:

    def test_search(self):
        res = search.Query('santos', country='ca')
        matches = res.list()
        assert is_match_for(NAME, matches[0][0]) == True
        assert is_match_for(NAME, matches[1][0]) == True
        assert is_match_for(WISHLIST, matches[0][1]) == True
        assert is_match_for(WISHLIST, matches[1][1]) == True


class TestSearchUKMultiple:

    def test_search(self):
        res = search.Query('santos', country='uk')
        matches = res.list()
        assert is_match_for(NAME, matches[0][0]) == True
        assert is_match_for(NAME, matches[1][0]) == True
        assert is_match_for(WISHLIST, matches[0][1]) == True
        assert is_match_for(WISHLIST, matches[1][1]) == True


class TestSearchESMultiple:

    def test_search(self):
        res = search.Query('santos', country='es')
        matches = res.list()
        assert is_match_for(NAME, matches[0][0]) == True
        assert is_match_for(NAME, matches[1][0]) == True
        assert is_match_for(WISHLIST, matches[0][1]) == True
        assert is_match_for(WISHLIST, matches[1][1]) == True


class TestSearchITMultiple:

    def test_search(self):
        res = search.Query('santos', country='it')
        matches = res.list()
        assert is_match_for(NAME, matches[0][0]) == True
        assert is_match_for(NAME, matches[1][0]) == True
        assert is_match_for(WISHLIST, matches[0][1]) == True
        assert is_match_for(WISHLIST, matches[1][1]) == True


class TestSearchFRMultiple:

    def test_search(self):
        res = search.Query('santos', country='fr')
        matches = res.list()
        assert is_match_for(NAME, matches[0][0]) == True
        assert is_match_for(NAME, matches[1][0]) == True
        assert is_match_for(WISHLIST, matches[0][1]) == True
        assert is_match_for(WISHLIST, matches[1][1]) == True


class TestSearchDEMultiple:

    def test_search(self):
        res = search.Query('santos', country='de')
        matches = res.list()
        assert is_match_for(NAME, matches[0][0]) == True
        assert is_match_for(NAME, matches[1][0]) == True
        assert is_match_for(WISHLIST, matches[0][1]) == True
        assert is_match_for(WISHLIST, matches[1][1]) == True


class TestSearchJPMultiple:

    def test_search(self):
        res = search.Query('santos', country='jp')
        matches = res.list()
        assert is_match_for(NAME, matches[0][0]) == True
        assert is_match_for(NAME, matches[1][0]) == True
        assert is_match_for(WISHLIST, matches[0][1]) == True
        assert is_match_for(WISHLIST, matches[1][1]) == True


class TestSearchCNMultiple:

    def test_search(self):
        res = search.Query('santos', country='cn')
        matches = res.list()
        assert is_match_for(NAME, matches[0][0]) == True
        assert is_match_for(NAME, matches[1][0]) == True
        assert is_match_for(WISHLIST, matches[0][1]) == True
        assert is_match_for(WISHLIST, matches[1][1]) == True


class TestSearchINMultiple:

    def test_search(self):
        res = search.Query('rajesh', country='in')
        matches = res.list()
        assert is_match_for(NAME, matches[0][0]) == True
        assert is_match_for(NAME, matches[1][0]) == True
        assert is_match_for(WISHLIST, matches[0][1]) == True
        assert is_match_for(WISHLIST, matches[1][1]) == True


# class TestSearchBrazilMultiple:
#    def test_search(self):
#        search = Search('caio1982@gmail.com', country='br')
#        matches = search.list()[0]
#        assert is_match_for(NAME, matches[0][0]) == True
#        assert is_match_for(NAME, matches[1][0]) == True
#        assert is_match_for(WISHLIST, matches[0][1]) == True
#        assert is_match_for(WISHLIST, matches[1][1]) == True
#
#
# class TestSearchMexicoMultiple:
#    def test_search(self):
#        search = Search('caio1982@gmail.com', country='mx')
#        matches = search.list()[0]
#        assert is_match_for(NAME, matches[0][0]) == True
#        assert is_match_for(NAME, matches[1][0]) == True
#        assert is_match_for(WISHLIST, matches[0][1]) == True
#        assert is_match_for(WISHLIST, matches[1][1]) == True
