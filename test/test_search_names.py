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


class TestSearchUSName:

    def test_search(self):
        res = search.Query('caio begotti', country='us')
        matches = res.list()
        assert is_match_for(NAME, matches[0][0]) == True


class TestSearchCAName:

    def test_search(self):
        res = search.Query('caio begotti', country='ca')
        matches = res.list()
        assert is_match_for(NAME, matches[0][0]) == True


class TestSearchUKName:

    def test_search(self):
        res = search.Query('caio begotti', country='uk')
        matches = res.list()
        assert is_match_for(NAME, matches[0][0]) == True


class TestSearchFRName:

    def test_search(self):
        res = search.Query('caio begotti', country='fr')
        matches = res.list()
        assert is_match_for(NAME, matches[0][0]) == True


class TestSearchDEName:

    def test_search(self):
        res = search.Query('caio begotti', country='de')
        matches = res.list()
        assert is_match_for(NAME, matches[0][0]) == True


class TestSearchITName:

    def test_search(self):
        res = search.Query('caio begotti', country='it')
        matches = res.list()
        assert is_match_for(NAME, matches[0][0]) == True


class TestSearchESName:

    def test_search(self):
        res = search.Query('caio begotti', country='es')
        matches = res.list()
        assert is_match_for(NAME, matches[0][0]) == True


class TestSearchJPName:

    def test_search(self):
        res = search.Query('caio begotti', country='jp')
        matches = res.list()
        assert is_match_for(NAME, matches[0][0]) == True


class TestSearchCNName:

    def test_search(self):
        res = search.Query('caio begotti', country='cn')
        matches = res.list()
        assert is_match_for(NAME, matches[0][0]) == True


class TestSearchINName:

    def test_search(self):
        res = search.Query('caio begotti', country='in')
        matches = res.list()
        assert is_match_for(NAME, matches[0][0]) == True


class TestSearchBrazilName:

   def test_search(self):
       res = search.Query('caio begotti', country='br')
       matches = res.list()
       assert is_match_for(NAME, matches[0][0]) == True


# class TestSearchMexicoName:
#    def test_search(self):
#        res = search.Query('caio begotti', country='mx')
#        matches = res.list()[0]
#        assert is_match_for(NAME, matches[0]) == True
