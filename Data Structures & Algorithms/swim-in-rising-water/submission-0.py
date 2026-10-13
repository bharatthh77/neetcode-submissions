class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        h = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0,0))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


        while h:
            cur, r, c = heapq.heappop(h)

            if (r,c) == (N-1, N-1):
                return cur

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if min(nr,nc) < 0 or nr >= N or nc >= N or (nr,nc) in visited:
                    continue

                visited.add((nr, nc))

                heapq.heappush(h, ((max(grid[nr][nc], cur)), nr, nc))

        
                



        