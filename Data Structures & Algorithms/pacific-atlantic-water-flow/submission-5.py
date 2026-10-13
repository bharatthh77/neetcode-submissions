class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW = len(heights)
        COL = len(heights[0])

        atlantic = set()
        pacific = set()

        def dfsAtl(i, j, prevI = None, prevj = None):
            if min(i,j) < 0 or i >= ROW or j >= COL or (i,j) in atlantic:
                return

            if (prevI is None and prevj is None) or (heights[i][j] >= heights[prevI][prevj]):
                atlantic.add((i,j))

                dfsAtl(i -1, j, i,j)
                dfsAtl(i+ 1, j, i,j)
                dfsAtl(i, j+1, i,j)
                dfsAtl(i, j-1, i,j)

        def dfsPac(i, j, prevI = None, prevj = None):
            if min(i,j) < 0 or i >= ROW or j >= COL or (i,j) in pacific:
                return

            if (prevI is None and prevj is None) or (heights[i][j] >= heights[prevI][prevj]):
                pacific.add((i,j))

                dfsPac(i -1, j, i,j)
                dfsPac(i+ 1, j, i,j)
                dfsPac(i, j+1, i,j)
                dfsPac(i, j-1, i,j)


        for i in range(ROW):
            dfsAtl(i, COL-1)

        for i in range(COL):
            dfsAtl(ROW -1, i)

        for i in range(ROW):
            dfsPac(i, 0)

        for i in range(COL):
            dfsPac(0, i)


        res = list(pacific.intersection(atlantic))

        return res
        