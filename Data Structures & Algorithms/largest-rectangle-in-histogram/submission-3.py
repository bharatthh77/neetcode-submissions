class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        res = 0

        for i, h in enumerate(heights):
            ind = i
            while st and st[-1][1] > h:
                curInd, curH = st.pop()
                res = max(res, (i-curInd) * curH)
                ind = curInd             
            st.append((ind,h))
        while st:
            curInd, curH = st.pop()
            res = max(res, (len(heights)-curInd) * curH)

        return res
            

        



