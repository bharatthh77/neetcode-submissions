class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(index, sol):

            if sum(sol) == target:
                res.append(sol[:])
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if sum(sol) + candidates[i] > target:
                    break

                sol.append(candidates[i])
                backtrack(i+1, sol)
                sol.pop()


        backtrack(0, [])

        return res

        