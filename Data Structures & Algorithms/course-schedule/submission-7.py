class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)

        for i, j in prerequisites:
            d[i].append(j)
            
        visited = set()
        visiting = set()
        
        def dfs(cur):
            if cur in visited:
                return True

            if cur in visiting:
                return False

            visiting.add(cur)
            for nei in d[cur]:
                if not dfs(nei):
                    return False

            visiting.remove(cur)
            visited.add(cur)
            return True

        for e in range(numCourses):
            if not dfs(e):
                return False

        return True

