class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(ind, curSum, curRes):
            if curSum == target:
                res.append(curRes[:])
                return

            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i-1]:
                    continue

                if (curSum + candidates[i]) > target:
                    break

                curRes.append(candidates[i])
                backtrack(i+1, curSum + candidates[i], curRes)
                curRes.pop()

        backtrack(0, 0, [])
        return res