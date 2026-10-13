# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(cur):
            if cur:
                res.append(cur.val)
            else:
                res.append('N')
                return
            
            dfs(cur.left)
            dfs(cur.right)
        dfs(root)

        res = [str(x) for x in res]
        ret = ','.join(res)
        print(ret)
        return ret

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        li = data.split(',')
        i = 0

        def dfs():
            nonlocal i

            if li[i] == 'N':
                i += 1
                return None
            
            cur = TreeNode(int(li[i]))
            i += 1
            cur.left = dfs()
            cur.right = dfs()

            return cur
        
        return dfs()
            

