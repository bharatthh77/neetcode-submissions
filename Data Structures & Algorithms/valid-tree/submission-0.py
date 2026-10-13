class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False

        d = defaultdict(list)

        for e in edges:
            d[e[0]].append(e[1])
            d[e[1]].append(e[0])

        visited = set()

        def dfs(cur, parent):
            if cur in visited:
                return False

            visited.add(cur)

            for e in d[cur]:
                if e == parent:
                    continue
                if not dfs(e, cur):
                    return False
            
            return True

    
        return dfs(0,-1) and len(visited) == n
            

        
