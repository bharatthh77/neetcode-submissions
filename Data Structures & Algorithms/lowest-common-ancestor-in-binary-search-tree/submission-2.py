# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        que = deque([root])

        while q:
            cur = que.popleft()

            if (p.val <= cur.val <= q.val) or (q.val <= cur.val <= p.val):
                return cur

            elif p.val < cur.val and q.val < cur.val:
                que.append(cur.left)
            
            elif p.val > cur.val and q.val > cur.val:
                que.append(cur.right)

        
            
        return None