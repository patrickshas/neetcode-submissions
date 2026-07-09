class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        shortened_price = prices
        for i in range(len(prices)-1):
            shortened_price = shortened_price [1:]
            sorted_shortened_price = sorted(shortened_price, reverse = True)

            profit_holder = sorted_shortened_price[0] - prices[i] 

            if profit_holder > profit:
                profit = profit_holder

        return profit
