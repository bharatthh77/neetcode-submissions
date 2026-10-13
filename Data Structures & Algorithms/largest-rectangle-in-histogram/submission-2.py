class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        res = 0

        for i,h in enumerate(heights):
            start = i
            while st and st[-1][0] > h:
                cur = st.pop()
                res = max(res, (i-cur[1]) * cur[0])
                start = cur[1]
            st.append((h, start))

        while st:
            cur = st.pop()
            res = max(res, cur[0] * (len(heights) - cur[1]))

        return res