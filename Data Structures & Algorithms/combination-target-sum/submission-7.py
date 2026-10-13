class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(index, sol):
            if sum(sol) > target:
                return

            if sum(sol) == target:
                res.append(sol[:])
                return
        
            for i in range(index, len(nums)):
                sol.append(nums[i])
                backtrack(i, sol)
                sol.pop()
    

        backtrack(0, [])

        return res