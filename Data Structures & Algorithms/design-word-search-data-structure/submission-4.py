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
            
            cur = root

            if index == len(word):
                return cur.isEnd

            print(f"word is: {word[index:]} and len is: {len(word[index:])} and cur is: {cur.val}")
            # if index == len(word):
            #     return root.isEnd

            c = word[index:index+1]
            index += 1
            print(f"c is: {c} cur is: {cur.val}")
            if c not in cur.characters and c != ".":
                return False
            
            if c in cur.characters and c != '.':
                return dfs(cur.characters[c], index)
            else:
                for e in cur.characters.values():
                    print(f"each is: {e.val}")
                    res = dfs(e, index)
                    if res:
                        return True
                return False
                        

        return dfs(self.root, 0)
        
