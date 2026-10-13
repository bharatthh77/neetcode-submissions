class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin = 1
        curMax = 1

        for num in nums:
            temp = curMin * num
            curMin = min(curMax * num, temp, num)
            curMax = max(temp, curMax * num, num)
            res = max(res, curMax)

        return res