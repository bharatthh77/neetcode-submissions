from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        
        def compare(a,b):
            if a+b > b+a:
                return -1
            else:
                return 1
        
        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int(''.join(nums)))


