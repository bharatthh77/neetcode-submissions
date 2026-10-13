class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        res = 0

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROW or c >= COL or grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            return (1 + 
            dfs(r + 1, c) + 
            dfs(r - 1, c) +
            dfs(r, c+1) +
            dfs(r, c-1))

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    res = max(res, dfs(i,j))

        return res

        