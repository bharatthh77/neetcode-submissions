class Solution:
    def maxArea(self, heights: List[int]) -> int:
            res = 0
            l = 0
            r = len(heights)-1
            while l<r:
                cur_res = min(heights[l],heights[r]) * (r-l)
                if cur_res > res:
                    res = cur_res
                if heights[l] < heights[r]:
                    l += 1
                else:
                    r -= 1
            return res

                


