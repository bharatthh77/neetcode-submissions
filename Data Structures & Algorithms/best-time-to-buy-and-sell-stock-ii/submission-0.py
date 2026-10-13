class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        for i, p in enumerate(prices):
            if i + 1 < n and prices[i+1] > p:
                res += prices[i+1] - p
            

        return res
