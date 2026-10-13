class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = l + (r-l)//2
            print(f'mid is: {mid}')

            if (nums[mid-1] if mid > 0 else -100000) < nums[mid] and nums[mid] > (nums[mid+1] if mid < len(nums)-1 else -100000):
                return mid
            
            elif nums[mid] < (nums[mid+1] if mid < len(nums)-1 else -100000):
                l = mid + 1

            elif nums[mid] < (nums[mid-1] if mid > 0 else -100000):
                r = mid -1
            
        return len(nums) -1
