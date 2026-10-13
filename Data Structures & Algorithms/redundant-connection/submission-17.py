class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        d = defaultdict(list)

        for e in edges:
            d[e[0]].append(e[1])
            d[e[1]].append(e[0])

        visiting = set()
        cycleStart = -1
        cycle = set()

        def dfs(cur, parent):
            nonlocal cycleStart
            # print(cur)
            if cur in visiting:
                cycleStart = cur
                return

            visiting.add(cur)
            for e in d[cur]:
                if e == parent:
                    continue

                if not dfs(e, cur):
                    if cycleStart != -1:
                        cycle.add(cur)
                    if cur == cycleStart:
                        cycleStart = -1
                    return 
            return True

        dfs(1, -1)

        # print(visiting)
        # print(cycle)

        for i,j in reversed(edges):
            if i in cycle and j in cycle:
                return [i,j]
        


            






        