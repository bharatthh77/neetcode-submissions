class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = set()
        pacific = set()
        ROW = len(heights)
        COL = len(heights[0])

        def dfsAtl(i,j, prev_i = None, prev_j = None):
            # print('atl: ', i, j)
            
            if min(i, j) < 0 or i >= ROW or j >= COL or (i,j) in atlantic:
                return 
    
            if (prev_i is None and prev_j is None) or heights[i][j] >= heights[prev_i][prev_j]:
                atlantic.add((i,j))
                # print('atl set: ', atlantic)
                dfsAtl(i-1, j, i, j)
                dfsAtl(i, j+1, i, j)
                dfsAtl(i+1, j, i, j)
                dfsAtl(i, j-1, i, j)

        def dfsPac(i,j, prev_i = None, prev_j = None):
            # print('pac: ', i, j)
            if min(i, j) < 0 or i >= ROW or j >= COL or (i,j) in pacific:
                return 

            if (prev_i is None and prev_j is None) or heights[i][j] >= heights[prev_i][prev_j]:
                pacific.add((i,j))
                # print('pac set: ', pacific)
                dfsPac(i-1, j, i, j)
                dfsPac(i, j+1, i, j)
                dfsPac(i+1, j, i, j)
                dfsPac(i, j-1, i, j)

        for i in range(ROW):
            dfsAtl(i, COL-1)

        for i in range(COL):
            dfsAtl(ROW-1, i)

        for i in range(ROW):
            dfsPac(i, 0)

        for i in range(COL):
            dfsPac(0, i)

        # print('pac set final: ', pacific)
        # print('atl set final: ', atlantic)
        
        res_set = pacific.intersection(atlantic)
        # print(res_set)

        res = []
        for r,c in res_set:
            res.append([r,c])

        return res
