class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -float('inf')
        curSum = 0

        for e in nums:
            curSum += e
            res = max(res, curSum)
            if curSum < 0:
                curSum = 0

        return res
            
            

        