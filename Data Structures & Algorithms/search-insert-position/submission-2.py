class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + ((r-l)//2) 
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid-1
                if l > r and r >= 0:
                    return mid
                elif l > r and r < 0:
                    return 0
            elif nums[mid] < target:
                l = mid+1
                if l > r:
                    return l
            
        