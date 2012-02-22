COUNTRY_CONFIGS = {
    'us': {
      'currency': 'USD',
      'domain'  : '.com',
      'symbol'  : ur'\u0024',
    },
    'uk': {
      'currency': 'GBP',
      'domain'  : '.co.uk',
      'symbol'  : ur'\u00a3'
    },
    'ca': {
      'currency': 'CDN',
      'domain'  : '.ca',
      'symbol'  : ur'\u0024'
    },
    'fr': {
      'currency': 'EUR',
      'domain'  : '.fr',
      'symbol'  : ur'\u20ac'
    },
    'it': {
      'currency': 'EUR',
      'domain'  : '.it',
      'symbol'  : ur'\u20ac'
    },
    'es': {
      'currency': 'EUR',
      'domain'  : '.es',
      'symbol'  : ur'\u20ac'
    },
    'de': {
      'currency': 'EUR',
      'domain'  : '.de',
      'symbol'  : ur'\u20ac'
    },
    'jp': {
      'currency': 'JPY',
      'domain'  : '.jp',
      'symbol'  : ur'\uffe5'
    },
    'cn': {
      'currency': 'CNY',
      'domain'  : '.cn',
      'symbol'  : ur'\uffe5'
    }
}

def countryParams(country):
    if COUNTRY_CONFIGS.has_key(country):
        return COUNTRY_CONFIGS[country]
    else:
        raise Exception("Country not found or country parameter not present")
