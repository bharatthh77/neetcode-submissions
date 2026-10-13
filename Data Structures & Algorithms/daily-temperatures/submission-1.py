class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while st and temp > st[-1][0]:
                
                cur = st.pop()
                # print(cur)
                res[cur[1]] = i - cur[1]

            st.append((temp, i))
            # print(res)

        return res