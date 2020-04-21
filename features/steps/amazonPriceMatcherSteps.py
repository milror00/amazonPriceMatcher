import logging

from behave import given, when, then

from features.configuration.configuration import Configuration
from features.pages.AmazonProductPage import AmazonProductPage


@given(u'I have a uk product url {text}')
def step_impl(context,text):
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    config = Configuration()
    page = AmazonProductPage()
    context.productURL = text
    page.getURL(context, config.getAmazonCountryURL('uk') + text)


@then(u'the price in the uk is reported to stdout')
def step_impl(context):
    page = AmazonProductPage()
    price = page.getProductPriceByCountry(context, 'uk');
    print(context.productURL + ' price: ' + price + '  country: UK')

@then(u'the price in {text} is reported to stdout')
def step_impl(context, text):
    page = AmazonProductPage()
    price = page.getProductPriceByCountry(context, text);
    floatPrice = float(price.replace(' €','').replace(',','.'))/context.exchangeRate
    print(context.productURL + ' price: ' + price + '      £' + "{:.2f}".format(floatPrice)+ '  country: ' + text)


@given(u'the euro price is {text}')
def step_impl(context, text):
   context.exchangeRate = float(text)