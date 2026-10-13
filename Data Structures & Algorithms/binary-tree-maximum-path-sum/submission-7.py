# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(cur):
            nonlocal res
            if not cur:
                return 0

            left = dfs(cur.left)
            right = dfs(cur.right)

            left = max(0, left)
            right = max(0, right)

            res = max(res, left + right + cur.val)

            return cur.val + max(left, right)

        dfs(root)

        return res