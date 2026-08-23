class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0 
        
        for sell in prices:
            profit = sell - buy
            res = max(res, profit)
            buy = min(buy, sell)
        return res


