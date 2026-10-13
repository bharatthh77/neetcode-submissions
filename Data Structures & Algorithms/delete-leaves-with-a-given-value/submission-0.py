# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(cur):
            if not cur:
                return False

            if dfs(cur.left):
                cur.left = None

            if dfs(cur.right):
                cur.right = None

            if not cur.left and not cur.right:
                if cur.val == target:
                    return True
                else:
                    return False
        if dfs(root):
            return None

        return root

        