class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(i, curRes):
            if i == n:
                res.append(curRes[:])
                return 
            
            backtrack(i +1, curRes)
            curRes.append(nums[i])

            backtrack(i + 1, curRes)

            curRes.pop()

        backtrack(0, [])

        return res




        
        