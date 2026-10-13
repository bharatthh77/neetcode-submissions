# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        if not root:
            return 0
        
        def dfs(cur, max_lens):
            if not cur:
                return 0

            nonlocal res

            if(cur.val >= max(max_lens)):
                res += 1
            
            max_lens.append(cur.val)

            dfs(cur.left, max_lens)
            if cur.left:
                max_lens.pop()

            dfs(cur.right, max_lens)
            if cur.right:
                max_lens.pop()

        dfs(root, [root.val])

        return res
            
            

