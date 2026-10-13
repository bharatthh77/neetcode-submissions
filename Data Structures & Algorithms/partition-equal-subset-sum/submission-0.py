class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            temp = []
            for e in dp:
                tot = e + nums[i]
                if tot == target:
                    return True
                temp.append(tot)

            for e in temp:
                dp.add(e)
        
        return False