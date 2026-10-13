class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if not st:
                st.append((t, i))
            elif st:
                if t <= st[-1][0]:
                    st.append((t, i))
                else:
                    while st and t > st[-1][0]:
                        cur, ind = st.pop()
                        res[ind] = i - ind
                    st.append((t, i))
        return res
                        

        