class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        nodeCopy = Node(node.val)

        d = {node: nodeCopy}
        q = deque([node])

        while q:
            cur = q.popleft()

            for n in cur.neighbors:
                if n not in d:
                    d[n] = Node(n.val)
                    q.append(n)

                d[cur].neighbors.append(d[n])

        return nodeCopy