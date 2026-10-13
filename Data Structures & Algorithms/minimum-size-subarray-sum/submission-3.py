class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        res = float('inf')
        curSum = 0

        while r < len(nums):
            curSum += nums[r]
            # print(l, r, curSum, res)

            while l <= r and curSum >= target:
                res = min(res, r - l + 1)
                # print('min', l, r, curSum, res)
                curSum -= nums[l]
                l += 1
            
            r += 1

        return res if res != float('inf') else 0
            
            
        
            


        