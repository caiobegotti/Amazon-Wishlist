# -*- coding: utf-8 -*-
# Copyright (C) 2012 - Caio Begotti <caio1982@gmail.com>
# Distributed under the GPLv2, see the LICENSE file.

"""
Configuration module listing currently available store parameters.
"""

COUNTRY_CONFIGS = {
    'us': {
        'currency': 'USD',
        'domain': '.com',
        'symbol': ur'\u0024'
    },
    'uk': {
        'currency': 'GBP',
        'domain': '.co.uk',
        'symbol': ur'\u00a3'
    },
    'ca': {
        'currency': 'CDN',
        'domain': '.ca',
        'symbol': ur'\u0024'
    },
    'fr': {
        'currency': 'EUR',
        'domain': '.fr',
        'symbol': ur'\u20ac'
    },
    'it': {
        'currency': 'EUR',
        'domain': '.it',
        'symbol': ur'\u20ac'
    },
    'es': {
        'currency': 'EUR',
        'domain': '.es',
        'symbol': ur'\u20ac'
    },
    'de': {
        'currency': 'EUR',
        'domain': '.de',
        'symbol': ur'\u20ac'
    },
    'jp': {
        'currency': 'JPY',
        'domain': '.jp',
        'symbol': ur'\u00a5'
    },
    'cn': {
        'currency': 'CNY',
        'domain': '.cn',
        'symbol': ur'\uffe5'
    },
    'br': {
        'currency': 'BRL',
        'domain': '.com.br',
        'symbol': ur'\u0024'
    },
    'mx': {
        'currency': 'MXN',
        'domain': '.com.mx',
        'symbol': ur'\u0024'
    },
    'in': {
        'currency': 'INR',
        'domain': '.in',
        'symbol': ur'\u20B9'
    }
}


def available():
    """
    Returns a list with all the domain codes from stores currently supported.
    """
    stores = list(COUNTRY_CONFIGS)

    # as of now kindle-only, no wishlists
    stores.remove('mx')

    return stores


def country_params(country):
    """
    Returns a big dictionary with all stores' parameters within each own
    dictionary, including its code, currency code, currency symbol and domain.
    """
    if country in COUNTRY_CONFIGS:
        return COUNTRY_CONFIGS[country]
    else:
        raise Exception("Country not found or country parameter not present")
