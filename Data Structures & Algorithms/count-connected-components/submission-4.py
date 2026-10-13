class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(list)

        for e in edges:
            d[e[0]].append(e[1])
            d[e[1]].append(e[0])

        visited = set()

        res = 0
        
        def dfs(cur, parent):
            if cur in visited:
                return

            visited.add(cur)

            for e in d[cur]:
                if e == parent:
                    continue
                dfs(e, cur)

        for i in range(n):
            if i in visited:
                continue
            res += 1
            dfs(i, -1)

        return res