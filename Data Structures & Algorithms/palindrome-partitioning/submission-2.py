class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(ind, curRes):
            if ind >= len(s):
                res.append(curRes.copy())

            for i in range(ind, len(s)):
                curStr = s[ind: i + 1]

                if self.isValid(curStr):
                    curRes.append(curStr)
                    backtrack(i + 1, curRes)
                    curRes.pop()

        backtrack(0, [])
        return res

    def isValid(self, cur):
        return cur == cur[::-1]
        