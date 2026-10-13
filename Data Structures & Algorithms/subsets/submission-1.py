class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(ind, curRes):
            if ind == len(nums):
                res.append(curRes[:])
                return
            
            backtrack(ind + 1, curRes)
            curRes.append(nums[ind])
            backtrack(ind + 1, curRes)
            curRes.pop()

        backtrack(0, [])
        return res
        