# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(cur, curMax):
            nonlocal res

            if not cur:
                return

            elif cur.val >= curMax:
                res += 1

            curMax = max(cur.val, curMax)

            dfs(cur.left, curMax)

            dfs(cur.right, curMax)

    
        dfs(root, root.val)

        return res
            
