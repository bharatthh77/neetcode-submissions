class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        l = 0
        r = 0
        cur = 0
        while r < len(nums):
            if nums[r] == 1:
                cur += 1
            else:
                l = r + 1
                cur = 0
            r += 1 
            res = max(res, cur)
        return res
        