class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        pre_prices = [0] * n
        suf_prices = [0] * n
        min_prices = prices[0]
        max_prices = prices[n-1]
        max_profit = 0

        for i in range(n):
            if prices[i] < min_prices:
                min_prices = prices[i]
            pre_prices[i] = min_prices

        for i in range(n-1, -1, -1):
            if prices[i] > max_prices:
                max_prices = prices[i]
            suf_prices[i] = max_prices

        for i in range(n):
            profit = suf_prices[i] - pre_prices[i]
            max_profit = max(max_profit, profit)
        return max_profit