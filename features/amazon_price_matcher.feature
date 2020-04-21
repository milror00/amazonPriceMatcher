# Created by Oem at 20/04/2020
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
    |/Bose-Noise-Cancelling-Headphones-Black/dp/B07Q9MJKBV/                