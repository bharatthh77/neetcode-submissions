# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSameTree(self, root, subRoot):
            if not root and not subRoot:
                return True
            
            if root and not subRoot or subRoot and not root:
                return False
            
            if root.val != subRoot.val:
                return False
            else:
                return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root and not subRoot:
            return True
        
        if not root and subRoot:
            return False
            
        if not subRoot:
            return True

        q = deque([root])

        res = False

        while q:
            cur = q.popleft()

            if cur.val == subRoot.val:
                res = self.isSameTree(cur, subRoot)

            if res: 
                return True
            
            if cur.left:
                q.append(cur.left)

            if cur.right:
                q.append(cur.right)

        return res            

            




        
            
