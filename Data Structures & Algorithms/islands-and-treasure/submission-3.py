class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        q = deque()

        def addCell(i, j):
            if min(i, j) < 0 or i >= ROW or j >= COL or grid[i][j] == -1 or (i,j) in visited:
                return
            
            q.append([i,j])
            visited.add((i,j))

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visited.add((i,j))


        dist = 0
        while q:
            for i in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = dist
                addCell(i-1, j)
                addCell(i, j+1)
                addCell(i+1, j)
                addCell(i, j-1)
            dist += 1
                