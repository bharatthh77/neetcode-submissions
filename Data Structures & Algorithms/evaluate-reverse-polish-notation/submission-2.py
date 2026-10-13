class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opSet = set(['-', '+', '*', '/'])
        st = []

        for t in tokens:
            if t not in opSet:
                st.append(t)
            else:
                num1 = int(st.pop())
                num2 = int(st.pop())
                res = ''
                if t == '+':
                    res = num1 + num2
                elif t == '-':
                    res = num2 - num1
                elif t == '*':
                    res = num1 * num2
                elif t == '/':
                    res = int(num2/num1)
                st.append(str(res))

        return int(st[-1])   