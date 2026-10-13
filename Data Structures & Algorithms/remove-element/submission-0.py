class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        tot = len(nums)
        i = 0
        while i < tot:
            if nums[i] == val:
                tot -= 1
                nums[i] = nums[tot]
            else:
                i += 1
        return tot