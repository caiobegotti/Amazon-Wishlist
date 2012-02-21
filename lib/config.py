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
      'currency': 'CAD',
      'domain'  : '.ca',
      'symbol'  : ur'\u0024'
    }
    # [...]
}

def countryParams(country):
    if COUNTRY_CONFIGS.has_key(country):
        return COUNTRY_CONFIGS[country]
    else:
        raise Exception("Country not found or country parameter not present")