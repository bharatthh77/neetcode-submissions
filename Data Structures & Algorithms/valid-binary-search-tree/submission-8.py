# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, float('-inf'), float('inf'))])

        if not root:
            return True

        while q:
            cur, low, high = q.popleft()
            
            if not (low < cur.val < high):
                return False

            if cur.left:
                q.append((cur.left, low, cur.val))

            if cur.right:
                q.append((cur.right, cur.val, high))
            

        return True


        
        