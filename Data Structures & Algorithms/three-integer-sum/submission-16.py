class Solution:
    def twoSum(self, nums, target):
        s = set()
        res = set()

        for num in nums:
            diff = target - num

            if diff in s:
                res.add((num, diff))

            s.add(num)

        return res

    def threeSum(self, nums):
        nums.sort()
        res = set()

        i = 0

        while i < len(nums) and nums[i] <= 0:
            cur = nums[i]
            target = -cur

            pairs = self.twoSum(nums[i + 1:], target)

            for second, third in pairs:
                res.add(tuple(sorted((cur, second, third))))

            i += 1

        return [list(e) for e in res]