class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(ind, curSum, curRes):
            if curSum == target:
                res.append(curRes[:])
                return

            if curSum > target:
                return
            
            
            for i in range(ind, len(nums)):
                curRes.append(nums[i])
                curSum += nums[i]
                backtrack(i, curSum, curRes)
                curRes.pop()
                curSum -= nums[i]
                
        
        backtrack(0, 0, [])

        return list(res)

