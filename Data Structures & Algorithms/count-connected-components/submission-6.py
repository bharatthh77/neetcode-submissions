class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(list)

        for i,j in edges:
            d[i].append(j)
            d[j].append(i)


        res = 0

        visited = set()

        def dfs(cur, parent):
            if cur in visited:
                return 
            
            visited.add(cur)

            for nei in d[cur]:
                if nei == parent:
                    continue

                dfs(nei, cur)
        
        for i in range(n):
            if i in visited:
                continue
            res += 1

            dfs(i, -1)

        return res
            




        