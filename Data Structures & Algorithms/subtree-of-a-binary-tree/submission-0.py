# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque()
        if root:
            q.append(root)

        while q:
            cur = q.popleft()
            if self.isSameTree(cur, subRoot):
                return True
            if cur.left:
                q.append(cur.left)
            if cur.right: 
                q.append(cur.right)
        
        return False

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
        