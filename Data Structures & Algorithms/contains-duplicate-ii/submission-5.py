class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        r = 1

        while r < len(nums):
            if abs(r - l) > k:
                l += 1
                r = l + 1
                if l == r:
                    r += 1
                    continue
            if nums[l] == nums[r]:
                return True
            if r == len(nums) - 1:
                l += 1
                r = l + 1 
                continue           
            r += 1
        
        return False

            

            
            