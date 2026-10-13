class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        prod = 1
        for num in nums:
            if num != 0:
                prod *= num
            else: 
                zeroCount += 1
        
        if zeroCount >= 2:
            return [0] * len(nums)
        elif zeroCount == 1:
            res = []
            for num in nums:
                if num != 0:
                    res.append(0)
                else:
                    res.append(prod)
        elif zeroCount == 0:
            res = []
            for num in nums:
                res.append(prod// num)
        
        return res

            

