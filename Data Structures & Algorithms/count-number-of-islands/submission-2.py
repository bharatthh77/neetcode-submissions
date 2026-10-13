class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        res = 0

        def dfs(i,j):
            if i >= ROW or i < 0 or j >= COL or j < 0:
                return
            if grid[i][j] == '0':
                return

            grid[i][j] = '0'

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)


        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '1':
                    dfs(r,c)
                    res += 1
        return res