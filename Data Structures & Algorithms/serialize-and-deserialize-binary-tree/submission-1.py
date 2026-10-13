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
            if not cur:
                res.append('N')
                return
            else:
                res.append(str(cur.val))

            dfs(cur.left)
            dfs(cur.right) 
        dfs(root)

        str_res = ",".join(res)
        print(str_res)

        return str_res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        i = 0
        li = data.split(',')

        def dfs():
            nonlocal i
            cur = None

            if li[i] == 'N':
                i += 1
                return None
            else:
                cur = TreeNode(li[i])

            i +=1

            cur.left = dfs()
            cur.right = dfs()
            
            return cur

        return dfs()

