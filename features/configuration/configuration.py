class Configuration:

    def getEnvironment(self):
        return 'LIVE'

    def getBrowserType(self):
        return 'FIREFOX'


    def getAmazonCountryURL(self, country):
        if country == 'uk':
            return 'https://amazon.co.uk'
        if country == 'de':
            return 'https://amazon.de'
        elif country == 'es':
            return 'https://amazon.es'
        elif country == 'fr':
            return 'https://amazon.fr'
        elif country == 'it':
            return 'https://amazon.it'
        else:
            print("Uknown country: " + country)

    def getTimeOut(self):
        return 10
