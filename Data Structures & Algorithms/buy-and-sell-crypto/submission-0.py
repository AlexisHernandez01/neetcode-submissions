class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = prices[0]
        maxProfit = 0
        currPrice = 0
        profit = 0
        L = 0

        for R in range(len(prices)):
            currPrice = prices[R]
            profit = currPrice - minPrice
            minPrice = min(minPrice, currPrice)
            maxProfit = max(maxProfit, profit)
        return maxProfit