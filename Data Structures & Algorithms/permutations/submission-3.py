class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curRes):
            if len(curRes) == len(nums):
                res.append(curRes.copy())
                return

            for ind in range(len(nums)):
                if nums[ind] in curRes:
                    continue
                
                curRes.append(nums[ind])
                backtrack(curRes)
                curRes.pop()

        for i in range(len(nums)):
            backtrack([nums[i]])

        return res