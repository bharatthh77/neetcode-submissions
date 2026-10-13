class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        def addCell(i, j):
            if min(i, j) < 0 or i >= ROW or j >= COL or grid[i][j] != 1:
                return
            grid[i][j] = 2
            q.append([i, j])


        q = deque()

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    q.append([i,j])


        time = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
            
                addCell(i + 1, j)
                addCell(i - 1,j)
                addCell(i, j+1)
                addCell(i, j-1)
            if q:
                time += 1

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    return -1
        return time

