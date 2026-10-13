class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i, n in enumerate(nums):

            if nums[i] > 0:
                break
            
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            l = i + 1
            r = len(nums) -1

            while l < r:            
                sum = nums[i] + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum  > 0:
                    r -= 1
                elif sum == 0:
                    res.add(tuple(sorted([nums[i], nums[l], nums[r]])))
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
   
        return [list(t) for t in res]
