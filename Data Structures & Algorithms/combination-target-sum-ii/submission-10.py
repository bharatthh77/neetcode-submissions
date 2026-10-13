class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, curSum, curRes):
            if target == curSum:
                res.append(curRes.copy())
                return

            if i >= len(candidates) or target < curSum:
                return 

            curRes.append(candidates[i])

            backtrack(i + 1, curSum + candidates[i], curRes)

            curRes.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            backtrack(i + 1, curSum, curRes)

        backtrack(0, 0, [])
        return res 
        