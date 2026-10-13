class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {'+', '-', '*', '/'}
        st = []
        for token in tokens:
            if token not in op:
                st.append(token)
            else:
                op1 = int(st.pop())
                op2 = int(st.pop())
                res = None
                if token == '+':
                    res = op1 + op2
                elif token == '-':
                    res = op2 - op1
                elif token == '*':
                    res = op1 * op2
                else: 
                    res = int(op2/op1)
                st.append(res)                
        return int(st[-1])

                    