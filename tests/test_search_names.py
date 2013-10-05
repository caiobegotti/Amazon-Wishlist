#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

from amazonwish.amazonwish import Search

#kindle-only for the moment, no wishlists
#
#class TestSearchBrazilName:
#    def test_search(self):
#        s = Search('caio begotti', country='br')
#        matches = s.list()[0]
#        assert matches[0] == 'Caio Begotti'
#
#class TestSearchMexicoName:
#    def test_search(self):
#        s = Search('caio begotti', country='mx')
#        matches = s.list()[0]
#        assert matches[0] == 'Caio Begotti'

class TestSearchUSName:
    def test_search(self):
        s = Search('caio begotti', country='us')
        matches = s.list()[0]
        assert matches[0] == 'Caio Begotti'

class TestSearchCAName:
    def test_search(self):
        s = Search('caio begotti', country='ca')
        matches = s.list()[0]
        assert matches[0] == 'Caio Begotti'

class TestSearchUKName:
    def test_search(self):
        s = Search('caio begotti', country='uk')
        matches = s.list()[0]
        assert matches[0] == 'Caio Begotti'

class TestSearchFRName:
    def test_search(self):
        s = Search('caio begotti', country='fr')
        matches = s.list()[0]
        assert matches[0] == 'Caio Begotti'

class TestSearchDEName:
    def test_search(self):
        s = Search('caio begotti', country='de')
        matches = s.list()[0]
        assert matches[0] == 'Caio Begotti'

class TestSearchITName:
    def test_search(self):
        s = Search('caio begotti', country='it')
        matches = s.list()[0]
        assert matches[0] == 'Caio Begotti'

class TestSearchESName:
    def test_search(self):
        s = Search('caio begotti', country='es')
        matches = s.list()[0]
        assert matches[0] == 'Caio Begotti'

class TestSearchJPName:
    def test_search(self):
        s = Search('caio begotti', country='jp')
        matches = s.list()[0]
        assert matches[0] == 'Caio Begotti'

class TestSearchCNName:
    def test_search(self):
        s = Search('caio begotti', country='cn')
        matches = s.list()[0]
        assert matches[0] == 'Caio Begotti'

class TestSearchINName:
    def test_search(self):
        s = Search('caio begotti', country='in')
        matches = s.list()[0]
        assert matches[0] == 'Caio Begotti'
