# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        def dfs(self, root):

            if not root:
                return 0

            left = dfs(self, root.left)
            right = dfs(self, root.right)

            if abs(left - right) <= 1:
                self.res = True and self.res
            else:
                self.res = False and self.res

            print(f"root: {root.val}, res: {1 + max(left, right)} ")

            return 1 + max(left, right)
    
        dfs(self, root)

        return self.res

             

            

