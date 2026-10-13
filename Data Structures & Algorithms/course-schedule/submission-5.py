class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)

        for e in prerequisites:
            d[e[0]].append(e[1])
        visiting = set()
        visited = set()

        def dfs(cur):
            if cur in visiting:
                return False

            # if cur not in d:
            #     return True

            if cur in visited:  
                return True

            visiting.add(cur)
            for e in d[cur]:
                if not dfs(e):
                    return False

            visiting.remove(cur)
            visited.add(cur)
            return True

        for e in range(numCourses):
            if not dfs(e):
                return False

        return True
