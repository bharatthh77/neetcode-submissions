class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(sol):
            if not self.isValid(sol) or sol.count('(') > n or sol.count(')') > n:
                return

            elif sol.count(')') == sol.count('(') and sol.count('(') == n:
                res.append(sol.copy())
                return

            sol.append('(')
            backtrack(sol)
            sol.pop()
            sol.append(')')
            backtrack(sol)
            sol.pop()
            
        backtrack([])

        print(res)

        return [''.join(e) for e in res]

    def isValid(self, s):
        if s.count(')') > s.count('('):
            return False
        return True
