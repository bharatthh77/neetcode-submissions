class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        res = 0
        fin = -float('inf')

        while r < len(nums):
            # print(l, r)
            res += nums[r]
            fin = max(fin, res)
            # print('fin', fin)
            # print(res)
            if res < 0 and r + 1 < len(nums):
                l = r + 1
                res = 0
                r = l
            else: 
                r += 1
            
        return fin

            