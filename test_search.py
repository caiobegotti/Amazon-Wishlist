#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

from amazonwish.amazonwish import Search

class TestSearchUnitedStates:
    def test_search(self):
        s = Search('caio1982@gmail.com', country='us')
        matches = s.list()[0]
        assert matches[0] == 'Caio Begotti'
        assert matches[1] == '3MCYFXCFDH4FA'

class TestSearchCanada:
    def test_search(self):
        s = Search('renata rocha', country='ca')
        matches = s.list()[0]
        assert matches[0] == 'Renata Rocha'
        assert matches[1] == '2OO8G9NM4QYQJ'
