class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        if goal == 0:
            return True

        for i in range(len(nums) -2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        
            if goal == 0:
                return True
        return False