class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dest in sorted(tickets, reverse=True):
            adj[src].append(dest)

        res =[]

        def dfs(cur):
            while adj[cur]:
                dest = adj[cur].pop()
                dfs(dest)
            res.append(cur)
            
        dfs("JFK")

        return res[::-1]
        
