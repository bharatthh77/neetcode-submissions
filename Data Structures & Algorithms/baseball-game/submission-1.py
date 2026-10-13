class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for op in operations:
            if op == '+':
                sc1, sc2 = st[-1], st[-2]
                new = int(sc1) + int(sc2)
                st.append(new)
            elif op == 'D':
                top = st[-1]
                new = (int(top) * 2)
                st.append(new)
            elif op == 'C':
                st.pop()
            else:
                st.append(op)
        return sum([int(e) for e in st])
            
        