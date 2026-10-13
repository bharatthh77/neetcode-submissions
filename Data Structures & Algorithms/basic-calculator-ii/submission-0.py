class Solution:
    def calculate(self, s: str) -> int:
        op = '+'
        num = 0
        st = []
        s = s.replace(' ', '')
        
        for i,e in enumerate(s):
            if e.isdigit():
                num = num * 10 + int(e)
            if (not e.isdigit()) or i == len(s)-1:
                if op == '+':
                    st.append(num)
                elif op == '-':
                    st.append(-num)
                elif op == '*':
                    st.append(st.pop() * num)
                else:
                    st.append(int(st.pop()/ num))
                op = e
                num = 0
        return sum(st)
