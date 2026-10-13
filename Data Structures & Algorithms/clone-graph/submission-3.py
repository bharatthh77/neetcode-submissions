"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        d = {}

        if not node:
            return None

        def dfs(cur):
            if cur not in d:
                d[cur] = Node(cur.val)

            for nei in cur.neighbors:
                if nei not in d:
                    dfs(nei)
                d[cur].neighbors.append(d[nei])

        dfs(node)

        return d[node]
        