class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)

        def dfs(start, end, cache):
            if start > end:
                return 0

            if cache[start] != -1:
                return cache[start]

            cache[start] = max((nums[start] + dfs(start + 2, end, cache)),
            dfs(start + 1, end, cache))

            return cache[start]

        cache1 = [-1] * len(nums)
        cache2 = [-1] * len(nums)

        return max(dfs(0, n-2, cache1), dfs(1, n-1, cache2))


