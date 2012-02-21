from config import Config

from lxml import etree
from lxml.html import tostring

def to_text(t):
    """Returns a plain text string from an element tree."""
    return tostring(t, encoding='utf-8', method='text', pretty_print=True) 

def to_html(t):
    """Returns a HTML string from an element tree."""
    return tostring(t, encoding='utf-8', method='html', pretty_print=True) 

class Profile():
    def readConfig(self, country):
        config = Config()
        params = config.countryParams(country)
        return params

    def downloadPage(self, params, id):
        domain = params['domain']
        userid = id
        url = 'http://www.amazon' + domain + '/wishlist/' + userid
        parser = etree.HTMLParser()
        tree = etree.parse(url, parser)
        return tree

    def basicInfo(self, page):
        """Returns the name of the wishlist owner and, if available, the address of its profile picture."""
        # wishlists are supposed to show a first name, so it's safe to assume it will never be null
        name = page.xpath("//td[@id='profile-name-Field']")
        ret = []
        for string in name:
            ret.append(to_text(string))
        photo = page.xpath("//div[@id='profile']/div/img/@src")
        if photo:
            ret.append(photo[0])
        return ret

    def wishlists(self, page):
        """Returns a list of wishlists codes for a given person."""
        lists = page.xpath("/html/body/div[5]/div[1]/div/div[1]/div/div[@id='profileBox']/div/div[@id='profile']/div[@id='regListpublicBlock']/div/h3/a")
        return lists

    def wishlistsDetails(self, page):
        """Returns a tuple with lists, the first with all wishlists codes and the second with their total number of items (i.e. wishlist size)."""
        retcodes = []
        retsizes = []
        codes = page.xpath("/html/body/div[5]/div[1]/div/div[1]/div/div[@id='profileBox']/div/div[@id='profile']/div[@id='regListpublicBlock']/div/@id")
        for c in codes:
            retcodes.append(c.replace('regListsList',''))
        sizes = page.xpath("/html/body/div[5]/div[1]/div/div[1]/div/div[@id='profileBox']/div/div[@id='profile']/div[@id='regListpublicBlock']/div/div/span[1]")
        for s in sizes:
            retsizes.append(to_text(s))
        return retcodes, retsizes


class Wishlist():
    def readConfig(self, country):
        config = Config()
        params = config.countryParams(country)
        return params

    def downloadPage(self, params, id):
        domain = params['domain']
        userid = id
        url = 'http://www.amazon' + domain + '/wishlist/' + userid + '/ref=cm_wl_act_print_o?' + '_encoding=UTF8&layout=standard-print&disableNav=1&visitor-view=1&items-per-page=1000'
        parser = etree.HTMLParser()
        tree = etree.parse(url, parser)
        return tree

    def authors(self, page):
        """Returns the authors names and co-writers for every item."""
        authors = page.xpath("/html/body/div[@id='printcfg']/div[@id='itemsTable']/div/form/table/tbody[*]/tr[1]/td[3]/div/span")
        ret = []
        for a in authors:
            ret.append(to_text(a).replace(' by ','').strip())
        return ret
    
    def titles(self, page):
        """Returns items titles, even if they are pretty long ones (like academic books or journals)."""
        titles = page.xpath("/html/body/div[@id='printcfg']/div[@id='itemsTable']/div/form/table/tbody[*]/tr[*]/td[*]/div/strong")
        ret = []
        for t in titles:
            ret.append(to_text(t).strip())
        return ret
    
    def prices(self, page):
        """Returns the price tags for every item in a wishlist."""
        prices = page.xpath("/html/body/div[@id='printcfg']/div[@id='itemsTable']/div/form/table/tbody[*]/tr[*]/td[@class='pPrice']/span/strong")
        ret = []
        for p in prices:
            ret.append(to_text(p).replace('$',''))
        return ret
    
    def via(self, page):
        """Returns the original web page from which the wished item was pulled, only for Universal items not from Amazon directly."""
        via = page.xpath("/html/body/div[@id='printcfg']/div[@id='itemsTable']/div/form/table/tbody[*]/tr[*]/td[*]/strong[2]")
        ret = []
        for v in via:
            ret.append(to_text(v).replace('www.',''))
        return ret
    
    def covers(self, page):
        """Returns the addresses of items pictures (e.g. book covers, albums pictures)."""
        covers = page.xpath("/html/body/div[@id='printcfg']/div[@id='itemsTable']/div/form/table/tbody[*]/tr[*]/td[*]/div[@class='pImage']/img/@src")
        ret = []
        for c in covers:
            ret.append(c)
        return ret
