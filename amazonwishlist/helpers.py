# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

"""
Python improved version of the old, buggy Perl module WWW::Amazon::Wishlist.
"""

import config

from lxml import etree
from lxml.html import tostring
from lxml.html import fromstring

# only for charset detection, enforcing unicode
# when lxml is completely shitty in doing that!
from BeautifulSoup import UnicodeDammit


def _decoder(data):
    """Simple helper to enforce a decent charset handling."""
    converted = UnicodeDammit(data, isHTML=True)
    if not converted.unicode:
        raise UnicodeDecodeError("Failed to detect encoding, tried [%s]", ', '.join(converted.triedEncodings))
    return converted.unicode


def _parser(url):
    """Simple helper function to parse a document, returning its etree."""
    parser = etree.HTMLParser()
    try:
        page = etree.parse(url, parser)
    except IOError:
        raise IOError("Failed to download page data, check your connection")

    try:
        stringfied = tostring(page)
    except:
        raise BaseException("LXML failed to serialise the ElementTree into a string!")

    return fromstring(_decoder(stringfied))


def _stripper(string):
    """Simple string helper to get rid of nasty chars detected in tests."""
    known = [u'\u200b',
             u'\x81\x8f',
             u'\xef\xbf',
             u'\xa5']
    for char in known:
        string = string.replace(char, '')
    return string.strip()


def _read_config(country):
    """Simple helper to return the configuration dictionaries of the module"""
    return config.country_params(country)
