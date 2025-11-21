def maxProfit(prices):
        if not prices:
            return 0
            
        profit = 0
        buy_price = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] > buy_price:
                profit += prices[i] - buy_price
            buy_price = prices[i]
        
        return profit

print(maxProfit([1,2,3,4,5]))