URL = "^http://.*amazon.*/images/.*\..*$"
WISHLIST = "^[0-9A-Z]{13}$"
NAME = "^[\w ]{1,}"
NUMBER = "^\d{1,}"
PRICE = "(\d+[.,]\d+)+"

def is_match_for(pattern, string):
    regex = re.compile(pattern)
    if regex.search(string):
        return True
    else:
        return False
