class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(index, sol):
            nonlocal res
            # print('index: ', index)
            sol.append(nums[index])
            # print('sol: ', sol)
            if len(sol) == len(nums):
                res.append(sol.copy())
                # print('res: ', res)
                return
            
            for i in range(len(nums)):
                if nums[i] in sol or i == index:
                    continue
                backtrack(i, sol)
                sol.pop()

        for i in range(len(nums)):
            backtrack(i, [])

        return res

        
        


          