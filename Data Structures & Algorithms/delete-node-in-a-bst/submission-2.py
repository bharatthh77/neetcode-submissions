# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        temp = None
        
        def dfs(cur):
            nonlocal temp
            if not cur or temp:
                return

            if cur.left and cur.left.val == key:
                if cur.left.right:
                    temp = cur.left.right
                cur.left = cur.left.left
            if cur.right and cur.right.val == key:
                if cur.right.right:
                    temp = cur.right.right
                cur.right = cur.right.left

            if not temp:
                dfs(cur.left)
                dfs(cur.right)
            else:
                insert(cur, temp)
                return

        
        def insert(cur, toInsert):
            if toInsert.val < cur.val: 
                if cur.left:
                    insert(cur.left, toInsert)
                else:
                    cur.left = toInsert

            elif toInsert.val > cur.val:
                if cur.right:
                    insert(cur.right, toInsert)
                else:
                    cur.right = toInsert

        if root and root.val == key:
            if root.left:
                temp = root.right
                root = root.left
                if temp:
                    insert(root, temp)
                return root
            else:
                return root.right
            
        dfs(root)

        return root