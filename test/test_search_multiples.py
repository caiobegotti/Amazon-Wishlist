#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from amazonwish.amazonwish import Search

#kindle-only for the moment, no wishlists
#
#class TestSearchBrazilMultiple:
#    def test_search(self):
#        s = Search('caio1982@gmail.com', country='br')
#        matches = s.list()[0]
#        assert matches[0] == 'Caio Begotti'
#
#class TestSearchMexicoMultiple:
#    def test_search(self):
#        s = Search('caio1982@gmail.com', country='mx')
#        matches = s.list()[0]
#        assert matches[0] == 'Caio Begotti'

class TestSearchUSMultiple:
    def test_search(self):
        s = Search('begotti', country='us')
        matches = s.list()
        assert matches[0][0] == 'Caio Begotti'
        assert matches[1][0] == 'Pedro Ivo de Brito Begotti'

class TestSearchCAMultiple:
    def test_search(self):
        s = Search('santos', country='ca')
        matches = s.list()
        assert matches[0][0] == "Wayne Santos'"
        assert matches[1][0] == "Catia Santos'"

class TestSearchUKMultiple:
    def test_search(self):
        s = Search('santos', country='uk')
        matches = s.list()
        assert matches[0][0] == "Pedro Santos'"
        assert matches[1][0] == "paulo santos'"

class TestSearchESMultiple:
    def test_search(self):
        s = Search('santos', country='es')
        matches = s.list()
        assert matches[0][0] == "Santos Merino's"
        assert matches[1][0] == "santos'"

class TestSearchITMultiple:
    def test_search(self):
        s = Search('santos', country='it')
        matches = s.list()
        assert matches[0][0] == 'Silvia Santos'
        assert matches[1][0] == 'Santos'

class TestSearchFRMultiple:
    def test_search(self):
        s = Search('santos', country='fr')
        matches = s.list()
        assert matches[0][0] == 'Santos'
        assert matches[1][0] == 'santos'

class TestSearchDEMultiple:
    def test_search(self):
        s = Search('santos', country='de')
        matches = s.list()
        assert matches[0][0] == "Sandra DOS SANTOS'"
        assert matches[1][0] == "Julia Santos'"

class TestSearchJPMultiple:
    def test_search(self):
        s = Search('santos', country='jp')
        matches = s.list()
        assert matches[0][0] == 'Sebastien Santos'
        assert matches[1][0] == 'Joao Santos'

class TestSearchCNMultiple:
    def test_search(self):
        s = Search('santos', country='cn')
        matches = s.list()
        assert matches[0][0] == 'santos chia'
        assert matches[1][0] == 'Victor Santos'

class TestSearchINMultiple:
    def test_search(self):
        s = Search('rajesh', country='in')
        matches = s.list()
        assert matches[0][0] == "rajesh's"
        assert matches[1][0] == "Rajesh's"
