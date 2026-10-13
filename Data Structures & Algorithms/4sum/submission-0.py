class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                l = j + 1
                r = n - 1
                while l < r:
                    tot = nums[l] + nums[r] + nums[j] + nums[i]
                    if  tot == target:
                        res.append([nums[l], nums[r], nums[i], nums[j]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]: 
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -=1 
                    elif tot < target:
                        l += 1
                    elif tot > target:
                        r -= 1
        return res
                



        