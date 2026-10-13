class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        
        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_count += 1
        if zero_count > 1:
            return [0] * len(nums)
        res = []
        for i, num in enumerate(nums):
            if zero_count == 1:
                if num != 0:
                    res.append(0)
                else:
                    res.append(product)
            else:
                res.append(product // num)
        return res