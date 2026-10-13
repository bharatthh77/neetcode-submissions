class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        l = 0
        r = len(prices) -1

        while l < r:
            print(prices[l], prices[r])
            print(res)
            if prices[l] >= prices[r]:
                if r-1 == l:
                    l += 1
                    r = len(prices) -1
                else: r -= 1
            elif prices[l] < prices[r]:
                res = max(res, prices[r] - prices[l])
                if r-1 == l:
                    l += 1
                    r = len(prices) -1
                else: r -= 1
        return res

        