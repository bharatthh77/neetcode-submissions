class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        nums.sort()

        def backtrack(index, sol):
            nonlocal res

            if index == len(nums):
                if sol not in res:
                    res.append(sol[:])
                return

            sol.append(nums[index])
            backtrack(index+1, sol)
            sol.pop()

            backtrack(index+1, sol)

        backtrack(0, sol)

        return res