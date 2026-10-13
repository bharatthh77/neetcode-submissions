class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = Counter(nums)

        for k in d:
            if d[k] > len(nums)//2:
                return k