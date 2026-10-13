class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(index, sol, total):
            if total == target:
                res.append(sol[:])
                return

            for i in range(index, len(candidates)):
                # Skip duplicate choices at the same level
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                # Since sorted, everything after this is also too large
                if total + candidates[i] > target:
                    break

                sol.append(candidates[i])
                backtrack(i + 1, sol, total + candidates[i])
                sol.pop()

        backtrack(0, [], 0)
        return res