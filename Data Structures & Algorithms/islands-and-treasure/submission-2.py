from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])
        INF = 2**31 - 1

        def bfs(r, c):
            queue = deque([(r, c, 0)])
            visited = {(r, c)}
            while queue:
                i, j, dist = queue.popleft()
                for di, dj in [(-1,0),(0,1),(1,0),(0,-1)]:
                    ni, nj = i+di, j+dj
                    if (0 <= ni < ROW and 0 <= nj < COL
                            and (ni, nj) not in visited
                            and grid[ni][nj] != -1):
                        visited.add((ni, nj))
                        grid[ni][nj] = min(grid[ni][nj], dist+1)
                        queue.append((ni, nj, dist+1))

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    bfs(i, j)