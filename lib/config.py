class Config:
    def countryParams(self, country=None):
        if 'us' in country:
            config = {
                      'currency': 'USD',
                      'domain'  : '.com',
                      'symbol'  : ur'\u0024',
                      } 
        elif 'uk' in country:
            config = {
                      'currency': 'GBP',
                      'domain'  : '.co.uk',
                      'symbol'  : ur'\u00a3'
                      } 
        elif 'ca' in country:
            config = {
                      'currency': 'CAD',
                      'domain'  : '.ca',
                      'symbol'  : ur'\u0024'
                      }
        elif 'fr' in country:
            config = {
                      'currency': 'EUR',
                      'domain'  : '.fr',
                      'symbol'  : ur'\u20ac',
                     }
        elif 'jp' in country:
            config = {
                      'currency': 'JPY',
                      'domain'  : '.jp',
                      'symbol'  : ur'\u00a5',
                     }
        elif 'de' in country:
            config = {
                      'currency': 'EUR',
                      'domain'  : '.de',
                      'symbol'  : ur'\u20ac',
                     }
        elif 'it' in country:
            config = {
                      'currency': 'EUR',
                      'domain'  : '.it',
                      'symbol'  : ur'\u20ac',
                     }
        elif 'es' in country:
            config = {
                      'currency': 'EUR',
                      'domain'  : '.es',
                      'symbol'  : ur'\u20ac',
                     }
        elif 'cn' in country:
            config = {
                      'currency': 'CNY',
                      'domain'  : '.cn',
                      'symbol'  : ur'\uffe5',
                     }
        else:
            exit('Missing country parameter (e.g. us, uk, ca etc)')
        return config
