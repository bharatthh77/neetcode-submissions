class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(i, sol):
            if i >= len(s):
                res.append(sol.copy())

            for ind in range(i, len(s)):
                curStr = s[i: ind+1]

                if self.isValid(curStr):
                    sol.append(curStr)
                    backtrack(ind+1, sol)
                    sol.pop()

        backtrack(0, [])
        return res


    def isValid(self, s):
        return s == s[::-1]




