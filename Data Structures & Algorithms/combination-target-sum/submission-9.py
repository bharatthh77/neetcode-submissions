class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, curRes, curSum):
            if curSum == target:
                res.append(curRes.copy())
                return

            if i >= len(nums) or curSum > target:
                return 

            curRes.append(nums[i])

            backtrack(i, curRes, curSum + nums[i])

            curRes.pop()

            backtrack(i + 1, curRes, curSum)


        backtrack(0, [], 0)

        return res
        