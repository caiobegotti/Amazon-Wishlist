# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

"""
Python improved version of the old, buggy Perl module WWW::Amazon::Wishlist.

Amazon-Wishlist lets you retrieve all information of your wishlist from
Amazon stores which have that feature (stores which are Kindle-only
do not). It comes with two sample applications to search and list data. It's
also quite useful if you want to know the total cost of your Amazon wishlist.

It's written using LXML and XPaths for better speed, readability. It supports the
Amazon stores in the US, Canada, UK, France, Spain, Italy, Germany, Japan, China
and India. Brazilian and Mexican stores also have built-in support though
they are not live yet.
"""

__author__ = "Caio Begotti <caio1982@gmail.com>"
