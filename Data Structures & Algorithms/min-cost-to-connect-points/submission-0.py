class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i +1, n):
                x2, y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        h = [(0,0)]
        visited = set()

        res = 0

        while h:
            dist, cur = heapq.heappop(h)

            if cur in visited:
                continue

            visited.add(cur)
            res += dist

            for d, e in adj[cur]:
                if e not in visited:
                    heapq.heappush(h, (d, e))

        return res


