import requests
from bs4 import BeautifulSoup
from lxml import html


class AmazoPriceMatcher():
    def __init__(self):
        self.amazonShops = ('https://amazon.co.uk',
                            'https://amazon.de',
                            'https://amazon.es',
                            'https://amazon.fr',
                            'https://amazon.it')
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; "
                                      "x64; rv:66.0) "
                                      "Gecko/20100101 Firefox/66.0",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept": "text/html,application/xhtml+xml,"
                                  "application/xml;q=0.9,*/*;q=0.8",
                        "DNT": "1", "Connection": "close",
                        "Upgrade-Insecure-Requests": "1"}

    def getURL(self, url):
        try:
            request = requests.get(url=url, headers=self.headers)
            request.encoding = 'utf-8'
            html = request.text
            self.page_bf = BeautifulSoup(html, 'lxml')
        except Exception as e:
            print(e)
            exit(1)

    def getAllPricesFromShops(self, url):
        self.getURL(url)
        price1 = self.page_bf.find('span', id='priceblock_saleprice')
        price2 = self.page_bf.find('span', id='priceblock_ourprice')
        price3 = self.page_bf.find('span', id='olp-upd-new-used-freeshipping')
        price4 = self.page_bf.find('span', id='olp-upd-used-freeshipping')
        if price1 is not None:
            return price1.text
        elif price2 is not None:
            return price2.text
        elif price3 is not None:
            return price3.text
        elif price4 is not None:
            return price4.text
        else:
            return '0'


if __name__ == '__main__':
    amazonShops = ('https://amazon.co.uk',
                   'https://amazon.de',
                   'https://amazon.es',
                   'https://amazon.fr',
                   'https://amazon.it')
    product = '/Bose-Noise-Cancelling-Headphones-Black/dp/B07Q9MJKBV/'
    matcher = AmazoPriceMatcher()
    prices = []
    for shop in amazonShops:
        result = matcher.getAllPricesFromShops(shop + product)
        prices.append(result.replace('£', '').replace('\xa0€', '').replace(',', '.'))
    print(prices)
