class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0 
        for i in prices:
            sell = i
            profit = sell - buy
            if profit <= 0:
                profit = 0
            elif res < profit:
                res = profit
            buy = min(buy,i)
        return res



        



