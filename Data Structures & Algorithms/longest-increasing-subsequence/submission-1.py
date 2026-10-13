class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1 for _ in range(len(nums))]
        res = 1

        def dfs(i):
            if i == len(nums) - 1:
                return 1
            
            if memo[i] != -1:
                return memo[i]

            LIS = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    LIS = max(LIS, 1 + dfs(j))

            memo[i] = LIS
            return LIS

        for i in range(len(nums)):
            res = max(res, dfs(i))

        return res
