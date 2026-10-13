class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)

        if tot % 2 != 0:
            return False

        tar = tot // 2

        dp = {}

        def dfs(i, target):

            if target == 0:
                return True

            if target <= 0 or i >= len(nums):
                return False


            if (i,target) in dp:
                return dp[(i, target)]

        
            if dfs(i+1, target):
                dp[(i, target)] = True
                return True
            
            dp[(i, target)] = dfs(i+1, target - nums[i])
            
            return dp[(i, target)]

        return dfs(0, tar)
            
            

            