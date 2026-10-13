class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        curRes = 0
        for num in nums:
            if num - 1 not in s:
                curRes += 1
                nextNum = num + 1
                while nextNum in s:
                    curRes += 1
                    nextNum += 1
                res = max(res, curRes)
                curRes = 0
        return res