from config import Config

from lxml import etree
from lxml.html import tostring

def to_text(t):
    return tostring(t, encoding='utf-8', method='text', pretty_print=True) 

def to_html(t):
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
        ret = []
        name = page.xpath("//td[@id='profile-name-Field']")
        # wishlists are supposed to show a first name, so it's safe to assume it will never be null
        for string in name:
            ret.append(to_text(string))
        photo = page.xpath("//div[@id='profile']/div/img/@src")
        if photo:
            ret.append(photo[0])
        return ret

    def wishlists(self, page):
        """Returns a list of wishlists codes for a given person"""
        lists = page.xpath("/html/body/div[5]/div[1]/div/div[1]/div/div[@id='profileBox']/div/div[@id='profile']/div[@id='regListpublicBlock']/div/h3/a")
        return lists

    def wishlistsDetails(self, page):
        codes = page.xpath("/html/body/div[5]/div[1]/div/div[1]/div/div[@id='profileBox']/div/div[@id='profile']/div[@id='regListpublicBlock']/div/@id")
        sizes = page.xpath("/html/body/div[5]/div[1]/div/div[1]/div/div[@id='profileBox']/div/div[@id='profile']/div[@id='regListpublicBlock']/div/div/span[1]")
        return codes, sizes


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
        authors = page.xpath("/html/body/div[@id='printcfg']/div[@id='itemsTable']/div/form/table/tbody[*]/tr[1]/td[3]/div/span")
        return authors
    
    def titles(self, page):
        titles = page.xpath("/html/body/div[@id='printcfg']/div[@id='itemsTable']/div/form/table/tbody[*]/tr[*]/td[*]/div/strong")
        return titles
    
    def prices(self, page):
        prices = page.xpath("/html/body/div[@id='printcfg']/div[@id='itemsTable']/div/form/table/tbody[*]/tr[*]/td[@class='pPrice']/span/strong")
        return prices
    
    def via(self, page):
        via = page.xpath("/html/body/div[@id='printcfg']/div[@id='itemsTable']/div/form/table/tbody[*]/tr[*]/td[*]/strong[2]")
        return via
    
    def covers(self, page):
        covers = page.xpath("/html/body/div[@id='printcfg']/div[@id='itemsTable']/div/form/table/tbody[*]/tr[*]/td[*]/div[@class='pImage']/img/@src")
        return covers
