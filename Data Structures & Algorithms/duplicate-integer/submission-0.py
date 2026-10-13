class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d ={}
        for num in nums:
            d[num] = d.get(num, 0) + 1
            if d[num] > 1:
                return True
        return False

