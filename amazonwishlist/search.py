# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

"""
Python improved version of the old, buggy Perl module WWW::Amazon::Wishlist.
"""

import helpers

class Search():

    """
    The Search() class is the one to be used if you don't know an
    user's wishlist ID and need to look them up by e-mail or their name.

    >>> from amazonwish.amazonwish import Search
    >>> search = Search('begotti', country='it')
    """

    def __init__(self, name, country):
        params = helpers._read_config(country)
        self.currency = params['currency']
        self.domain = params['domain']
        self.symbol = params['symbol']
        self.name = name
        self.country = country
        self.page = None
        self._download()

    def _download(self):
        """Builds a search query and retrieves its result for the parser."""
        query = ['/gp/registry/search.html?',
                 'ie=UTF8',
                 '&type=wishlist',
                 '&field-name=',
                 self.name]
        url = 'http://www.amazon' + self.domain + ''.join(query)
        self.page = helpers._parser(url)

    def list(self):
        """
        Returns a list with tuples containing all matching usernames
        and their main wishlist ID, with which you can get secondary
        lists via the Wishlist() class.

        >>> wishlists = search.list()
        >>> for row in wishlists:
        >>>     print row
        """
        # before pipe, page with usernames; after, single exact matches
        wishlists = self.page.xpath("//td/span/a//@href | //div[@id='sortbarDisplay']/form//@action")
        names = self.page.xpath("//td/span/a//text() | //h1[@class='visitor']//text()")
        names = [helpers._stripper(n) for n in names]

        codes = []
        for code in wishlists:
            codes.append(helpers._stripper(code.split('/')[3]))
        # FIXME: hack not to return empty search results,
        # whose only anchor text is not english
        if not 'tg' in codes:
            return zip(names, codes)
