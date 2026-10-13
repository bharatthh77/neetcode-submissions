class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        res =[]
        visiting = set()
        visited = set()
        
        for e in prerequisites:
            d[e[0]].append(e[1])

        def dfs(cur):
            if cur in visited:
                return True
            
            if cur in visiting:
                return False

            visiting.add(cur)

            for e in d[cur]:
                if not dfs(e):
                    return False
            
            visiting.remove(cur)
            visited.add(cur)
            res.append(cur)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return res
                
        


        

        
