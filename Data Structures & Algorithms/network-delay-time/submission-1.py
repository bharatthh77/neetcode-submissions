class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))

        d = {}
        h = [(0, k)]

        while h:
            time, cur = heapq.heappop(h)
            if cur in d:
                continue
            d[cur] = time

            for nei, t in adj[cur]:
                if nei not in d:
                    heapq.heappush(h, (time + t, nei))

        return max(d.values()) if len(d) == n else -1 

            
