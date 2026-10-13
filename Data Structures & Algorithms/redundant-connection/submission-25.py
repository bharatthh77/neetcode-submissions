class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        cycle = set()
        cycleStart = -1
        visited = set()

        d = defaultdict(list)

        for i, j in edges:
            d[i].append(j)
            d[j].append(i)

        def dfs(cur, parent):
            nonlocal cycleStart

            if cur in visited:
                cycleStart = cur
                return

            visited.add(cur)
            for e in d[cur]:
                if e == parent:
                    continue

                dfs(e, cur)

                if cycleStart != -1:
                    cycle.add(cur)
                    if cur == cycleStart:
                        cycleStart = -1
                    return

        dfs(1, -1)

        for i,j in reversed(edges):
            if i in cycle and j in cycle:
                return [i,j]



        


            

        