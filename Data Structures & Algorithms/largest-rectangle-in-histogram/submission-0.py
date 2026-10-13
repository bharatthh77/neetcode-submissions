class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        st = []
        for i,e in enumerate(heights):
            if st:
                if e >= st[-1][1]:
                    st.append((i, e))
                elif e < st[-1][1]:
                    cur = st[-1]
                    while st and e < st[-1][1]:
                        cur = st.pop()
                        curheight = cur[1] * (i - cur[0])
                        res = max(res , curheight)
                    st.append((cur[0], e))
            else:
                st.append((i, e))
            
        while st:
            cur = st.pop()
            curheight = cur[1] * (len(heights) - cur[0])
            res = max(res, curheight)

        return res

        

