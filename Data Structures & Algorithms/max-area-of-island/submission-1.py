class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        area = []

        def dfs(i, j):
            if i < 0 or j < 0 or i >= ROW or j >= COL:
                return
            
            if grid[i][j] != 1:
                return

            area[-1] += 1

            grid[i][j] = 0
            
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i+1, j)
            dfs(i, j-1)


        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    area.append(0)
                    dfs(i,j)
        
        if area:
            return max(area)
        else: 
            return 0
                       