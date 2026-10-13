# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st = []
        def dfs(cur):
            nonlocal st

            if not cur: 
                return
            
            if len(st) >= k:
                return

            dfs(cur.left)

            st.append(cur.val)

            dfs(cur.right)

        dfs(root)

        return st[k-1]
            