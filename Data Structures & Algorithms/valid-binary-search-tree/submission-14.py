# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(cur, maxVal, minVal):
            nonlocal res
            if not (minVal < cur.val < maxVal):
                res = False
                return

            if cur.left:
                dfs(cur.left, min(cur.val, maxVal), minVal)

            if cur.right:
                dfs(cur.right, maxVal, max(minVal, cur.val))

        dfs(root, float('inf'), float('-inf'))

        return res