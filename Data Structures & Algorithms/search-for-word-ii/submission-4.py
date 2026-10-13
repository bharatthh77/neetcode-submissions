class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEnd = False


    def addWord(self, word: str):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R = len(board)
        C = len(board[0])
        root = TrieNode()
        for word in words:
            root.addWord(word)

        res = set()
        visited = set()

        
        def dfs(r, c, word, node):
            if r < 0 or c < 0 or r >= R or c >= C or (r,c) in visited:
                return
            
            ch = board[r][c]

            if ch not in node.children:
                return

            visited.add((r,c))
            node = node.children[ch]
            word += ch

            if node.isEnd:
                res.add(word)
            

            dfs(r+1, c, word, node)
            dfs(r, c+1, word, node)
            dfs(r-1, c, word, node)
            dfs(r, c-1, word, node)

            visited.remove((r,c))


        for i in range(R):
            for j in range(C):
                dfs(i, j, "", root)

        return list(res)
        