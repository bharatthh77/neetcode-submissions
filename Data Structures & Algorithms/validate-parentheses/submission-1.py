class Solution:
    def isValid(self, s: str) -> bool:
        match = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for e in s:
            if e in match:
                stack.append(e)
            else: 
                if not stack or match[stack[-1]] != e:
                    return False
                else:
                    stack.pop()    
        return (not stack)