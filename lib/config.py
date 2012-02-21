class Config:
    def getCountryParams(self, country=None):
        if 'us' in country:
            config = {
                      'currency': 'USD',
                      'domain'  : '.com',
                      'symbol'  : ur'$',
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
                      'symbol'  : ur'$'
                      }
        else:
            exit('Missing country parameter (e.g. us, uk, ca etc)')
        return config
