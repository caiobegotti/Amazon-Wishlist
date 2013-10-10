#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

import sys
import os.path

# generic test helpers 
from test_utils_functions import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from amazonwish.amazonwish import Search


class TestSearchUSMultiple:

    def test_search(self):
        search = Search('begotti', country='us')
        matches = search.list()
        assert is_match_for(NAME, matches[0[0]]) == True
        assert is_match_for(NAME, matches[1[0]]) == True
        assert is_match_for(WISHLIST, matches[0][1]) == True
        assert is_match_for(WISHLIST, matches[1][1]) == True


class TestSearchCAMultiple:

    def test_search(self):
        search = Search('santos', country='ca')
        matches = search.list()
        assert is_match_for(NAME, matches[0[0]]) == True
        assert is_match_for(NAME, matches[1[0]]) == True
        assert is_match_for(WISHLIST, matches[0][1]) == True
        assert is_match_for(WISHLIST, matches[1][1]) == True


class TestSearchUKMultiple:

    def test_search(self):
        search = Search('santos', country='uk')
        matches = search.list()
        assert is_match_for(NAME, matches[0[0]]) == True
        assert is_match_for(NAME, matches[1[0]]) == True
        assert is_match_for(WISHLIST, matches[0][1]) == True
        assert is_match_for(WISHLIST, matches[1][1]) == True


class TestSearchESMultiple:

    def test_search(self):
        search = Search('santos', country='es')
        matches = search.list()
        assert is_match_for(NAME, matches[0[0]]) == True
        assert is_match_for(NAME, matches[1[0]]) == True
        assert is_match_for(WISHLIST, matches[0][1]) == True
        assert is_match_for(WISHLIST, matches[1][1]) == True


class TestSearchITMultiple:

    def test_search(self):
        search = Search('santos', country='it')
        matches = search.list()
        assert is_match_for(NAME, matches[0[0]]) == True
        assert is_match_for(NAME, matches[1[0]]) == True
        assert is_match_for(WISHLIST, matches[0][1]) == True
        assert is_match_for(WISHLIST, matches[1][1]) == True


class TestSearchFRMultiple:

    def test_search(self):
        search = Search('santos', country='fr')
        matches = search.list()
        assert is_match_for(NAME, matches[0[0]]) == True
        assert is_match_for(NAME, matches[1[0]]) == True
        assert is_match_for(WISHLIST, matches[0][1]) == True
        assert is_match_for(WISHLIST, matches[1][1]) == True


class TestSearchDEMultiple:

    def test_search(self):
        search = Search('santos', country='de')
        matches = search.list()
        assert is_match_for(NAME, matches[0[0]]) == True
        assert is_match_for(NAME, matches[1[0]]) == True
        assert is_match_for(WISHLIST, matches[0][1]) == True
        assert is_match_for(WISHLIST, matches[1][1]) == True


class TestSearchJPMultiple:

    def test_search(self):
        search = Search('santos', country='jp')
        matches = search.list()
        assert is_match_for(NAME, matches[0[0]]) == True
        assert is_match_for(NAME, matches[1[0]]) == True
        assert is_match_for(WISHLIST, matches[0][1]) == True
        assert is_match_for(WISHLIST, matches[1][1]) == True


class TestSearchCNMultiple:

    def test_search(self):
        search = Search('santos', country='cn')
        matches = search.list()
        assert is_match_for(NAME, matches[0[0]]) == True
        assert is_match_for(NAME, matches[1[0]]) == True
        assert is_match_for(WISHLIST, matches[0][1]) == True
        assert is_match_for(WISHLIST, matches[1][1]) == True


class TestSearchINMultiple:

    def test_search(self):
        search = Search('rajesh', country='in')
        matches = search.list()
        assert is_match_for(NAME, matches[0[0]]) == True
        assert is_match_for(NAME, matches[1[0]]) == True
        assert is_match_for(WISHLIST, matches[0][1]) == True
        assert is_match_for(WISHLIST, matches[1][1]) == True


# class TestSearchBrazilMultiple:
#    def test_search(self):
#        search = Search('caio1982@gmail.com', country='br')
#        matches = search.list()[0]
#        assert is_match_for(NAME, matches[0[0]]) == True
#        assert is_match_for(NAME, matches[1[0]]) == True
#        assert is_match_for(WISHLIST, matches[0][1]) == True
#        assert is_match_for(WISHLIST, matches[1][1]) == True
#
#
# class TestSearchMexicoMultiple:
#    def test_search(self):
#        search = Search('caio1982@gmail.com', country='mx')
#        matches = search.list()[0]
#        assert is_match_for(NAME, matches[0[0]]) == True
#        assert is_match_for(NAME, matches[1[0]]) == True
#        assert is_match_for(WISHLIST, matches[0][1]) == True
#        assert is_match_for(WISHLIST, matches[1][1]) == True
