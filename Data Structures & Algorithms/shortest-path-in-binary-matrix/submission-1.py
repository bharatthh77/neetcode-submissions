class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (+1, 0), (0, -1), (0, +1), (-1, -1), (+1, +1), (-1, +1), (+1, -1)]
        ROW = len(grid)
        COL = len(grid[-1])

        n = len(grid)

        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        q = deque([(0,0,1)])
        visited = set()
        

        while q:
            r, c, d = q.popleft()
            visited.add((r, c))
            if (r, c) == (n-1, n-1):
                return d
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    q.append((nr, nc, d + 1))
            
        return -1

