"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        oldToNew = {}

        def dfs(cur):
            # print(cur.val)

            if cur not in oldToNew:
                oldToNew[cur] = Node(cur.val)
            
            # for k,v in oldToNew.items():
            #     print(k.val, v.val)

            for nei in cur.neighbors:
                if nei not in oldToNew:
                    dfs(nei)
                oldToNew[cur].neighbors.append(oldToNew[nei])

        dfs(node)

        return oldToNew[node]


