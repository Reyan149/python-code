def calulate_total_profit(prices):
    totalprofit = 0

    for i in range(1, len(prices)):

        if prices[i] > prices[i - 1]:
            profit_from_this_jump = prices[i] - prices[i - 1]
            totalprofit += profit_from_this_jump

    return totalprofit
stock_prices = [1,4,1,4,1]
print('Total profit : ', calulate_total_profit(stock_prices))