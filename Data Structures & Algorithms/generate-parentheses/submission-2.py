class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(count, sol):
            nonlocal res

            if sol.count('(') > n or sol.count(')') > n or not self.isValid(sol[:]):
                return

            if len(sol) == 2 * n:
                res.append(''.join(sol))
                return

            sol.append('(')
            backtrack(count + 1, sol)
            sol.pop()

            sol.append(')')
            backtrack(count + 1, sol)
            sol.pop()

            
        backtrack(0, [])
        return res

    def isValid(self, st):
            if st.count(')') > st.count('('):
                return False
            return True    