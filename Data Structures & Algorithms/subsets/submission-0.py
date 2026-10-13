class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def backtrack(index, sol):
            nonlocal res

            if index == len(nums):
                res.append(sol[:])
                return

            sol.append(nums[index])
            backtrack(index+1, sol)
            sol.pop()

            backtrack(index+1, sol)

        backtrack(0, sol)

        return res