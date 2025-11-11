# Question 1 - Price Surge Alert
# 1300 1500 2700 1500 
# Output: 4
# Output: 7000

# Question 2 - Wallet Preview 
# 0x9F1aB3c...

# Question 3 - Portfolio Value
def portfolio_value(holdings, prices): 
    usd_value = 0.00
    for key, value in holdings.items(): 
        multiplied = value * prices[key]
        usd_value += multiplied
    return f"{usd_value:.2f}"

holdings = {"BTC": 0.5, "ETH": 8.2, "SOL": 50}
prices = {"BTC": 62400, "ETH": 2480, "SOL": 142}
print(portfolio_value(holdings, prices))