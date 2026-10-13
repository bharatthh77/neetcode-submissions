class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        cur = ''
        for e in s:
            # print('st: ', st)
            # print(e)
            if e != ']':
                st.append(e)
            elif e == ']':
                while st[-1] != '[':
                    cur = st.pop() + cur
                st.pop()
                mul = st.pop()
                while st and st[-1].isdigit():
                    mul = st.pop() + mul               
                cur *= int(mul)
                # print('cur: ', cur)
                st.append(cur)
                cur = ''
        return ''.join(st)
