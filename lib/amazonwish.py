from config import Config

from lxml import etree

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
        name = page.xpath("/html/body/div[5]/div[1]/div/div[1]/div/div[@id='profileBox']/div/div[@id='profile']/div[@id='profileInfo']/table/tbody/tr[1]/td[@id='profile-name-Field']")
        photo = page.xpath("/html/body/div[5]/div[1]/div/div[1]/div/div[@id='profileBox']/div/div[@id='profile']/div[1]/img/@src")
        return name, photo

    def wishlists(self, page):
        lists = page.xpath("/html/body/div[5]/div[1]/div/div[1]/div/div[@id='profileBox']/div/div[@id='profile']/div[@id='regListpublicBlock']/div/h3/a")
        return lists

    def wishlistsDetails(self, page):
        codes = page.xpath("/html/body/div[5]/div[1]/div/div[1]/div/div[@id='profileBox']/div/div[@id='profile']/div[@id='regListpublicBlock']/div/@id")
        size = page.xpath("/html/body/div[5]/div[1]/div/div[1]/div/div[@id='profileBox']/div/div[@id='profile']/div[@id='regListpublicBlock']/div/div/span[1]")
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
