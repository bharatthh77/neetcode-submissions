class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.binSearch(nums, True, target)
        r = self.binSearch(nums, False, target)

        return [l, r]


    def binSearch(self,nums, leftBias, target) -> int:
        l = 0
        r = len(nums) - 1

        i = -1
        while l <= r:
            mid = l + (r-l)//2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                i = mid
                if leftBias:
                    r = mid - 1
                else:
                    l = mid + 1
                
        return i


        