class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isEnd = False


class PrefixTree:

    def __init__(self):
        self.root = TreeNode(-1)


    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode(c)

            cur = cur.children[c]
        
        cur.isEnd = True



    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        
        return True if cur.isEnd else False
            

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
            
        return True
        
        