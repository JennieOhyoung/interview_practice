"""
I have an array stockPricesYesterday where the keys are the number of minutes into the day (starting with midnight) and the values are the price of Apple stock at that time. For example, the stock cost $500 at 1am, so stockPricesYesterday[60] = 500.
Write an efficient algorithm for computing the best profit I could have made from 1 purchase and 1 sale of an Apple stock yesterday.
"""

import random

def generate_stockprice():
    stock_prices_yesterday = {}
    # minutes_yesterday = 720
    minutes_yesterday = 20
    for minute in range(1, minutes_yesterday+1):
        stock_prices_yesterday[minute] = round(random.uniform(1,101), 2)
    return stock_prices_yesterday

def maximize_profit(stock_prices_yesterday):
    purchase_price = stock_prices_yesterday[1]
    profit = 0
    for minute in range(1, len(stock_prices_yesterday)+1):
        current_price = stock_prices_yesterday[minute]
        purchase_price = min(purchase_price, current_price)
        profit = max(profit, current_price - purchase_price)
    return profit




# print generate_stockprice()

print maximize_profit(generate_stockprice())
