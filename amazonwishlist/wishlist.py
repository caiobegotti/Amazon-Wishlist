# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

"""
Python improved version of the old, buggy Perl module WWW::Amazon::Wishlist.
"""

import helpers


class Wishlist():

    """
    The Wishlist() class is the main class of Amazon Wishlist as
    it's here where the magic happens. This class will retrieve
    through XPath expressions the titles of all items inside a
    wishlist, their authors and co-writers, price tags, covers
    (if books) or items picture, listing which external sources your
    wishlist uses and even the total amount necessary if you were
    to buy all the items at once.

    >>> from amazonwish.amazonwish import Wishlist
    >>> wishlist = Wishlist('3MCYFXCFDH4FA', country='us')
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
        """Retrieves and stores the printable version of the wishlist for later parsing."""
        query = ['/ref=cm_wl_act_print_o?',
                 '_encoding=UTF8',
                 '&layout=standard-print',
                 '&disableNav=1',
                 '&visitor-view=1',
                 '&items-per-page=9999']
        url = 'http://www.amazon' + self.domain + '/wishlist/' + self.userid + ''.join(query)
        self.page = helpers._parser(url)

    def authors(self):
        """Returns the authors names, co-writers or manufacturers for every item.

        >>> authors = wishlist.authors()
        """
        ret = []
        attr = ('de ', 'di ', 'by ', 'von ')
        for author in self.page.xpath("//div[@class='pTitle']"):
            subtree = helpers.tostring(author, encoding='unicode', method='html', pretty_print=True)
            if 'span' in subtree:
                parser = helpers.etree.HTMLParser()
                div = helpers.etree.fromstring(subtree, parser)
                res = div.xpath("//span[@class='small itemByline']//text()")
                for author in res:
                    author = author.replace('~', '').strip()
                    if author.startswith(tuple(attr)):
                        author = author[3:].strip()
                        ret.append(helpers._stripper(author))
                    else:
                        ret.append(helpers._stripper(author))
            else:
                ret.append(ur'')
        dirt = ['DVD', 'VHS']
        for item in dirt:
            while item in ret:
                ret.remove(item)
        return ret

    def titles(self):
        """
        Returns items titles, even if they are pretty long
        ones (like academic books or journals).

        >>> titles = wishlist.titles()
        """
        ret = []
        for title in self.page.xpath("//div[@class='pTitle']/strong//text()"):
            ret.append(helpers._stripper(title))
        return ret

    def prices(self):
        """Returns the price tags for every item in a wishlist.

        >>> prices = wishlist.prices()
        """
        prices = self.page.xpath("//td[@class='pPrice'][not(text()) and not(strong)] | //td[@class='pPrice']/strong[3] | //td[@class='pPrice']/strong[1] | //td[@class='Price']/span/strong//text()")

        # cleanups, every store has different price tag extras
        if 'EUR' in self.currency:
            dust = 'EUR'
        elif 'CDN' in self.currency:
            dust = 'CDN' + ur'\u0024'
        elif 'GBP' in self.currency:
            dust = ur'\u00a3'
        elif 'INR' in self.currency:
            dust = 'Rs. '
        elif 'CNY' in self.currency:
            dust = u'\xa5'
        elif 'JPY' in self.currency:
            dust = u'\x81\x8f'
        else:
            dust = self.symbol

        ret = []
        for price in prices:
            res = helpers.tostring(price, encoding='unicode', method='text', pretty_print=True).strip()
            if 'At' not in res:
                # TODO: how would it work out for non-english stores? quite a huge bug ahead...
                if 'Click' in res:
                    res = ''
                if 'EUR' in self.currency or 'BRL' in self.currency:
                    res = res.replace(dust, '')
                    res = res.replace('.', '')
                    res = res.replace(',', '.')
                else:
                    res = res.replace(dust, '')
                    res = res.replace(',', '')
                ret.append(helpers._stripper(res))
        return ret

    def via(self):
        """
        Returns the sorted original web pages from which the wished item was
        pulled, only for Universal items not sold by Amazon directly.

        >>> via = wishlist.via()
        """
        ret = []
        for url in self.page.xpath("//div/form/table/tbody[*]/tr[*]/td[*]/strong[2]//text()"):
            ret.append(helpers._stripper(url))
        ret = sorted(list(set(ret)))
        return ret

    def covers(self):
        """Returns the addresses of items pictures (e.g. book covers, albums pictures).

        >>> covers = wishlist.covers()
        """
        ret = []
        for filename in self.page.xpath("//div/form/table/tbody[*]/tr[*]/td[*]/div[@class='pImage']/img/@src"):
            filename = filename.split('.')
            filename = '.'.join(filename[:-2]) + '.' + filename[-1]
            ret.append(helpers._stripper(filename))
        return ret

    def urls(self):
        """Returns the page address of a given item in the wishlist, with its full details.

        >>> urls = wishlist.urls()
        """
        ret = []
        for url in self.page.xpath("//tbody[@class='itemWrapper']//@name"):
            if 'item' in url:
                code = url.split('.')[3]
                if code:
                    res = 'http://www.amazon' + self.domain + '/dp/' + code
                else:
                    res = ''
                ret.append(helpers._stripper(res))
        return ret

    def ideas(self):
        """Returns a list of ideas to shop for later, as reminders

        >>> ideas = wishlist.ideas()
        """
        ret = []
        ideas = [ur'Idea',
                 ur'Idee',
                 ur'Id\xc3\xa9e',
                 ur'\xe8\xa7\x82\xe5\xbf\xb5',
                 ur'Id\xc3\xa9ia']
        for row in zip(self.titles(), self.prices()):
            if row[1] in ideas:
                ret.append(helpers._stripper(row[0]))
        return ret

    def total_expenses(self):
        """
        Returns the total sum of all prices (with no currency or locale setting),
        not considering unavailable items or items with no price tags.

        >>> total = wishlist.total_expenses()
        """
        tags = []
        ideas = [ur'Idea',
                 ur'Idee',
                 ur'Id\xc3\xa9e',
                 ur'\xe8\xa7\x82\xe5\xbf\xb5',
                 ur'Id\xc3\xa9ia']
        prices = self.prices()
        for tag in prices:
            if tag in ideas:
                prices.remove(tag)
        for price in filter(None, prices):
            if price.count('.') > 1:
                price = price.replace('.', '', (price.count('.') - 1))
            tags.append(float(price))
        ret = sum(tags)
        return ret
