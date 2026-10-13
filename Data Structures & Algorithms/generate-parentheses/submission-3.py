class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curRes):
            if not self.isValid(curRes[:]) or curRes.count(')') > n or curRes.count('(') > n :
                return 

            if len(curRes) == 2 * n:
                res.append(curRes[:])
                return

            curRes.append('(')
            backtrack(curRes)
            curRes.pop()

            curRes.append(')')
            backtrack(curRes)
            curRes.pop()

        backtrack([])

        return [''.join(e) for e in res]
    
    def isValid(self, cur):
        if cur.count(')') > cur.count('('):
            return False
        return True