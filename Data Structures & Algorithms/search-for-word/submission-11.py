class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False

        ROW = len(board)
        COL = len(board[0])
        visited = set()

        def backtrack(r, c, curWord, k):
            nonlocal res
            if res == True:
                return

            if curWord == word:
                res = True
                return

            if min(r,c) < 0 or r >= ROW or c >= COL or board[r][c] != word[k] or (r,c) in visited:
                return

            visited.add((r,c))

            curWord += word[k]
            k += 1

            backtrack(r + 1, c, curWord, k)
            backtrack(r, c+1, curWord, k)
            backtrack(r-1, c, curWord, k)
            backtrack(r, c-1, curWord, k)

    
            visited.remove((r,c))
        

        for i in range(ROW):
            for j in range(COL):
                backtrack(i, j, '', 0)

        return res





        