#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from amazonwish.amazonwish import Search


class TestSearchUS:

    def test_search(self):
        search = Search('caio1982@gmail.com', country='us')
        matches = search.list()[0]
        assert matches[0] == 'Caio Begotti'
        assert matches[1] == '3MCYFXCFDH4FA'


class TestSearchCanada:

    def test_search(self):
        search = Search('caio1982@gmail.com', country='ca')
        matches = search.list()[0]
        assert matches[0] == 'Caio Begotti'
        assert matches[1] == 'PEK9J1M112UK'


class TestSearchUK:

    def test_search(self):
        search = Search('caio1982@gmail.com', country='uk')
        matches = search.list()[0]
        assert matches[0] == 'Caio Begotti'
        assert matches[1] == 'MBI8TEEYJS10'


class TestSearchGermany:

    def test_search(self):
        search = Search('caio1982@gmail.com', country='de')
        matches = search.list()[0]
        assert matches[0] == 'Caio Begotti'
        assert matches[1] == '2ZPN6SBGBP4X8'


class TestSearchItaly:

    def test_search(self):
        search = Search('caio1982@gmail.com', country='it')
        matches = search.list()[0]
        assert matches[0] == 'Caio Begotti'
        assert matches[1] == '3W1RQNDJTCQC'


class TestSearchFrance:

    def test_search(self):
        search = Search('caio1982@gmail.com', country='fr')
        matches = search.list()[0]
        assert matches[0] == 'Caio Begotti'
        assert matches[1] == '2POKVB3027QIK'


class TestSearchSpain:

    def test_search(self):
        search = Search('caio1982@gmail.com', country='es')
        matches = search.list()[0]
        assert matches[0] == 'Caio Begotti'
        assert matches[1] == '1LJ10M7BWAICD'


class TestSearchJapan:

    def test_search(self):
        search = Search('caio1982@gmail.com', country='jp')
        matches = search.list()[0]
        assert matches[0] == 'Caio Begotti'
        assert matches[1] == '13RB1XNS2VF62'


class TestSearchChina:

    def test_search(self):
        search = Search('caio1982@gmail.com', country='cn')
        matches = search.list()[0]
        assert matches[0] == 'Caio Begotti'
        assert matches[1] == '3BFG9M3CL83QR'

# kindle-only for the moment, no wishlists
#
# class TestSearchBrazil:
#    def test_search(self):
#        search = Search('caio1982@gmail.com', country='br')
#        matches = search.list()[0]
#        assert matches[0] == 'Caio Begotti'
#        assert matches[1] == ''
#
# class TestSearchMexico:
#    def test_search(self):
#        search = Search('caio1982@gmail.com', country='mx')
#        matches = search.list()[0]
#        assert matches[0] == 'Caio Begotti'
#        assert matches[1] == ''


class TestSearchIndia:

    def test_search(self):
        search = Search('caio1982@gmail.com', country='in')
        matches = search.list()[0]
        assert matches[0] == 'Caio Begotti'
        assert matches[1] == 'ZVKVJQHOBAT2'


class TestSearchUSMultiple:

    def test_search(self):
        search = Search('begotti', country='us')
        matches = search.list()
        assert matches[0][0] == 'Caio Begotti'
        assert matches[1][0] == 'Pedro Ivo de Brito Begotti'
