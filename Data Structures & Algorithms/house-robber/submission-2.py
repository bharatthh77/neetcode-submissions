class Solution:
    def rob(self, nums: List[int]) -> int:
        totalcost = [0] * len(nums)
        if len(nums) < 3:
            return(max(nums))

        totalcost[0] = nums[0]
        totalcost[1] = nums[1]
        
        totalcost[2] = totalcost[0] + nums[2]

        if len(nums) < 4:
            return(max(totalcost))

        for i in range(3, len(nums)):
            totalcost[i] = nums[i] + max(totalcost[i-2], totalcost[i-3])

        return max(totalcost)