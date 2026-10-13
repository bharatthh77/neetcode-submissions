# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(cur):
            if not cur:
                return 0

            leftMax = dfs(cur.left)
            rightMax = dfs(cur.right)

            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)

            res[0] = max(res[0], (leftMax + rightMax + cur.val))
            return cur.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
            
