class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(index, sol):
            sol.append(nums[index])

            if sum(sol) > target:
                return

            if sum(sol) == target:
                res.append(sol[:])
        
            for i in range(index, len(nums)):
                backtrack(i, sol)
                sol.pop()
    

        for i in range(len(nums)):
            backtrack(i, [])

        return res