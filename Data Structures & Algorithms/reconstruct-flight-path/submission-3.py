class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(deque)
        for src, dest in sorted(tickets):
            adj[src].append(dest)

        res = []

        def dfs(cur):
            while adj[cur]:
                nei = adj[cur].popleft()
                dfs(nei)


            res.append(cur)

        dfs('JFK')

        return res[::-1]
