class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROW = len(grid)
        COL = len(grid[0])

        def dfs(i, j):
            # print(i,j)
            # print(grid)
            if i < 0 or j < 0 or i >= ROW or j >= COL:
                return

            if grid[i][j] != '1':
                return

            grid[i][j] = '0'

            dfs(i - 1, j)

            dfs(i, j + 1)
            
            dfs(i + 1, j)

            dfs(i, j - 1)

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i,j)
                else:
                    continue
        
        return res
                
                    
                
        
            
        
        
