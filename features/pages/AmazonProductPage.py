import lxml
import requests
import urllib3
from io import BytesIO
from lxml import etree
from lxml import html

from features.configuration.configuration import Configuration

class AmazonProductPage():

    def getURL(self, context, url):
        http = urllib3.PoolManager()
        context.response = http.request('GET', url)


    def getProductPriceByCountry(self,context , country):
        config = Configuration()
        self.getURL(context, config.getAmazonCountryURL(country) + context.productURL)
        dom = lxml.html.parse(BytesIO(context.response.data))
        # all table rows
        xpatheval = etree.XPathDocumentEvaluator(dom)
        price = xpatheval('.//*[@id="olp-upd-new-used-freeshipping"]/a/span')
        if len(price) > 0:
            return price[0].text
        price = xpatheval('.//*[@id="olp-upd-new-used-freeshipping"]/a/span')
        if len(price) > 0:
            return price[0].text
        price = xpatheval('.//*[@id="olp-upd-used-freeshipping"]/a/span')
        if len(price) > 0:
            return price[0].text
        price = xpatheval('.//*[@id="priceblock_ourprice"]')
        if len(price) > 0:
            return price[0].text
        price = xpatheval('.//*[@id="priceblock_saleprice"]')
        if len(price) > 0:
            return price[0].text
        return '0'
