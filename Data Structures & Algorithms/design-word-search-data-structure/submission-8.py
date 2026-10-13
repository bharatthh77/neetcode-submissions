class TreeNode:
    def __init__(self, val):
        self.val = val
        self.characters = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode("-1")
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.characters:
                cur.characters[c] = TreeNode(c)
            cur = cur.characters[c]
        cur.isEnd = True


    def search(self, word: str) -> bool:

        def dfs(root, index):
            if index == len(word):
                if root.isEnd:
                    return True
                else:
                    return False
            curChar = word[index]

            if curChar != '.' and curChar not in root.characters:
                return False
            elif curChar not in root.characters and curChar == '.':
                for e in root.characters.values():
                    if dfs(e, index + 1):
                        return True
                return False
            elif curChar in root.characters:
                return dfs(root.characters[curChar], index + 1)


        return dfs(self.root, 0)
        
