# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True

        if not p and not q:
            return True

        if p and not q or q and not p:
            return False 
        
        que = deque([(p, q)])

        while que:
            cur1, cur2 = que.popleft()

            if cur1.val != cur2.val:
                return False

            if cur1.left and cur2.left:
                que.append((cur1.left, cur2.left))
            
            if cur1.left and not cur2.left or cur2.left and not cur1.left:
                return False

            if cur1.right and cur2.right:
                que.append((cur1.right, cur2.right))
            
            if cur1.right and not cur2.right or cur2.right and not cur1.right:
                return False
            
        return res


            

        

