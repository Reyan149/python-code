def max_profit(prices):
    if not prices:
        return
    
    min_price = prices[0]
    max_profit = 0

    for current_price in prices[1:]:
        if current_price < min_price:
            min_price = current_price
        
        potential_profit = current_price - min_price

        if potential_profit > max_profit:
            max_profit = potential_profit

    return max_profit

stock_prices = [7, 1, 5, 3, 6, 4]
print('Maximum profit:', max_profit(stock_prices))