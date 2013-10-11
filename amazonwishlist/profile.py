# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

"""
Python improved version of the old, buggy Perl module WWW::Amazon::Wishlist.

"""

import helpers


class Profile():

    """
    The Profile() class is the one responsible for retrieving
    information about a given user, such as name, profile photo,
    existing wishlists and their names and size.

    >>> from amazonwish.amazonwish import Profile
    >>> person = Profile('3MCYFXCFDH4FA', country='us')
    """

    def __init__(self, userid, country):
        params = helpers._read_config(country)
        self.currency = params['currency']
        self.domain = params['domain']
        self.symbol = params['symbol']
        self.userid = userid
        self.country = country
        self.page = None
        self._download()

    def _download(self):
        """
        Retrieves and stores the profile page (i.e. first wishlist
        page plus user's information and other wishlists details).
        """
        url = 'http://www.amazon' + self.domain + '/wishlist/' + self.userid
        self.page = helpers._parser(url)

    def basic_info(self):
        """
        Returns the name of the wishlist owner and, if available,
        the address of its profile picture.

        >>> info = person.basic_info()
        """
        # wishlists are supposed to show a first name, so it's safe to assume it will never be null
        ret = []
        for name in self.page.xpath("//td[@id='profile-name-Field']//text()"):
            ret.append(helpers._stripper(name))

        photo = self.page.xpath("//div[@id='profile']/div/img/@src")
        if photo:
            filename = photo[0].split('.')
            filename = '.'.join(filename[:-2]) + '.' + filename[-1]
            ret.append(helpers._stripper(filename))

        return ret

    def wishlists(self):
        """Returns a list of wishlists codes for a given person.

        >>> lists = person.wishlists()
        """
        return self.page.xpath("//div[@id='profile']/div[@id='regListpublicBlock']/div/h3/a//text()")

    def wishlists_details(self):
        """
        Returns a tuple with lists, the first with all wishlists
        codes and the second with their total number of items
        (i.e. wishlist size).

        >>> details = person.wishlists_details()
        """
        retcodes = []
        for code in self.page.xpath("//div[@id='profile']/div[@id='regListpublicBlock']/div/@id"):
            retcodes.append(helpers._stripper(code.replace('regListsList', '')))

        retsizes = []
        for size in self.page.xpath("//div[@id='profile']/div[@id='regListpublicBlock']/div/div/span[1]//text()"):
            retsizes.append(helpers._stripper(size))

        return retcodes, retsizes
