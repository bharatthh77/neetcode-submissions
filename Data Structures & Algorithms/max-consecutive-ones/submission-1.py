class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0

        l = 0

        for r in range(len(nums)):
            if nums[l] == 1 and nums[r] == 1:
                res = max(res, len(nums[l : r+1]))
            elif nums[l] != 1:
                l += 1
                r = l
            elif nums[r] != 1:
                l = r + 1
                r = l
        return res
            
