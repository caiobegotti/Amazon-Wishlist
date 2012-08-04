#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

import re

import web
from web import form

from amazonwish.config import *

from amazonwish.amazonwish import Search
from amazonwish.amazonwish import Profile
from amazonwish.amazonwish import Wishlist

render = web.template.render( 'templates/', base='layout')

urls = (
    '/(.*)', 'index'
)

form = form.Form(
    form.Textbox('get',
                 form.notnull,
                 description='',
                 size='50'
                 ))

app = web.application(urls, globals(), True)

class index:        
    def GET(self, term):
        res = web.input()
        if res:
            s = Search(res['get'], country='us')
            wishlist = s.list()[0][1]

            p = Profile(wishlist, country='us')
            info = p.basicInfo()          
            
            wl = Wishlist(wishlist, country='us')
            total = wl.total_expenses()
            covers = wl.covers()
            urls = wl.urls()
            titles = wl.titles()
            authors = wl.authors()
            prices = wl.prices()
            items = zip(covers, urls, titles, authors, prices)

            return render.result(s.list(), total, info, items, wl.currency)
        else:
            f = form()
            return render.form(f)

#web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)

if __name__ == "__main__":
    #web.runwsgi = web.runfcgi
    app.run()
