class Solution:
    def maxProfit(self, prices):
        max_Profit, min_price = 0, float('inf')
        for i in range(len(prices)):
            profit = prices[i] - min_price
            max_Profit = max(profit, max_Profit)
            min_price = min(min_price, prices[i])
        return max_Profit

sol = Solution()
print(sol.maxProfit([7, 1, 6, 0 ,3]))
print(sol.maxProfit([9, 4, 6, 8]))