# Amazon Price Matcher
This is a demo project that uses python - request, behave to scrape the product prices published on the amazon uk, de, fr, it and es sites.
for a specified product.This is a demo to demonstrate the skills I have for scraping. 

This code is not to be used for any reason commercial or personally other than to demonstrate the approach to scraping.

Requirements to run :

Python 3.7 above

behave==1.2.6

requests==2.23.0

lxml==4.5.0

idna==2.9

urlib3==1.25.9

Steps for installation:

Clone git repo

I use PyCharm Professional to I import the project which creates a virtual environment for the project

Install libraries : pip install behave pip install requests pip install lxml

Open the console at the root of project and run the command :

behave ./features

Feature: To compare the prices for the same product in different countries

  Scenario Outline: Get the price for an item

    Given I have a uk product url <productURL>
    
    And the euro price is 1.14
    
    Then the price in the uk is reported to stdout
    
    Then the price in de is reported to stdout
    
    And the price in es is reported to stdout
    
    And the price in fr is reported to stdout
    
    And the price in it is reported to stdout

  Examples:
  
    |productURL                                                            |
    
    |/Bose-Noise-Cancelling-Headphones-Black/dp/B07Q9MJKBV/                |
    
    
   Here is the output :
   
   /Bose-Noise-Cancelling-Headphones-Black/dp/B07Q9MJKBV/ price: £279.89  country: UK
   
/Bose-Noise-Cancelling-Headphones-Black/dp/B07Q9MJKBV/ price: 269,00 €      £235.96  country: de

/Bose-Noise-Cancelling-Headphones-Black/dp/B07Q9MJKBV/ price: 289,00 €      £253.51  country: es

/Bose-Noise-Cancelling-Headphones-Black/dp/B07Q9MJKBV/ price: 319,00 €      £279.82  country: fr

/Bose-Noise-Cancelling-Headphones-Black/dp/B07Q9MJKBV/ price: 399,95 €      £350.83  country: it


