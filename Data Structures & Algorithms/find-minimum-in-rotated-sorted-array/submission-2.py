class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1
        min_res = float('inf')

        while l <= r:
            mid = l + (r-l)//2
            if nums[l] <= nums[mid]:
                min_res = min(min_res, nums[l])
                l = mid + 1 
            else:
                min_res = min(min_res, nums[mid])
                r = mid - 1
        return min_res

            