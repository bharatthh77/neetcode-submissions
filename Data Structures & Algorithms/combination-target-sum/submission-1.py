class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(index, sol):
            sol.append(nums[index])

            # print('index: ', index)
            # print('sol: ', sol)
            # print('res: ', res)

            if sum(sol) == target:
                res.append(sol[:])
                # sort_sol = sorted(sol)
                # if sort_sol not in res:
                #     res.append(sort_sol)
            
            if sum(sol) > target:
                return

            for i in range(index, len(nums)):
                backtrack(i, sol)
                sol.pop()

        for e in range(len(nums)):
            backtrack(e, [])
        return res