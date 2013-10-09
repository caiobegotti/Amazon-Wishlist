#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from amazonwish.amazonwish import Search

# kindle-only for the moment, no wishlists
#
# class TestSearchBrazilName:
#    def test_search(self):
#        search = Search('caio begotti', country='br')
#        matches = search.list()[0]
#        assert matches[0] == 'Caio Begotti'
#
# class TestSearchMexicoName:
#    def test_search(self):
#        search = Search('caio begotti', country='mx')
#        matches = search.list()[0]
#        assert matches[0] == 'Caio Begotti'


class TestSearchUSName:

    def test_search(self):
        search = Search('caio begotti', country='us')
        matches = search.list()[0]
        assert matches[0] == 'Caio Begotti'


class TestSearchCAName:

    def test_search(self):
        search = Search('caio begotti', country='ca')
        matches = search.list()[0]
        assert matches[0] == 'Caio Begotti'


class TestSearchUKName:

    def test_search(self):
        search = Search('caio begotti', country='uk')
        matches = search.list()[0]
        assert matches[0] == 'Caio Begotti'


class TestSearchFRName:

    def test_search(self):
        search = Search('caio begotti', country='fr')
        matches = search.list()[0]
        assert matches[0] == 'Caio Begotti'


class TestSearchDEName:

    def test_search(self):
        search = Search('caio begotti', country='de')
        matches = search.list()[0]
        assert matches[0] == 'Caio Begotti'


class TestSearchITName:

    def test_search(self):
        search = Search('caio begotti', country='it')
        matches = search.list()[0]
        assert matches[0] == 'Caio Begotti'


class TestSearchESName:

    def test_search(self):
        search = Search('caio begotti', country='es')
        matches = search.list()[0]
        assert matches[0] == 'Caio Begotti'


class TestSearchJPName:

    def test_search(self):
        search = Search('caio begotti', country='jp')
        matches = search.list()[0]
        assert matches[0] == 'Caio Begotti'


class TestSearchCNName:

    def test_search(self):
        search = Search('caio begotti', country='cn')
        matches = search.list()[0]
        assert matches[0] == 'Caio Begotti'


class TestSearchINName:

    def test_search(self):
        search = Search('caio begotti', country='in')
        matches = search.list()[0]
        assert matches[0] == 'Caio Begotti'
