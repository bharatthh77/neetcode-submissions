class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        visited = set()

        d = defaultdict(list)
        for i,j in edges:
            d[i].append(j)
            d[j].append(i)

        def dfs(cur, parent):
            if cur in visited:
                return False

            visited.add(cur)

            for nei in d[cur]:
                if nei == parent:
                    continue

                if not dfs(nei, cur):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n
        