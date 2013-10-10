import re

URL = "^http://.*amazon.*/images/.*\.[A-Za-z]{3,5}$"
WISHLIST = "^[0-9A-Z]{10,}$"
NAME = "^[\w ']{1,}"
NUMBER = "^\d{1,}"
PRICE = "^((\d{1,3}[.,])+\d{1,2})$"
DP = "^http://www.amazon.*/dp/[0-9A-Z]{10,}$"
VIA = "^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?"
TITLE = "^[\w\W\s]+$|^$"

def is_match_for(pattern, string):
    regex = re.compile(pattern)
    if regex.search(string):
        return True
    else:
        return False
