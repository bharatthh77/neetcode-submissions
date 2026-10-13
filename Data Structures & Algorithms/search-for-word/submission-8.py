class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])
        res = False
        visited = set()

        def backtrack(r, c, ind):
            nonlocal res

            if len(word) <= ind or r >= ROW or c >= COL or min(r,c) < 0 or board[r][c] != word[ind] or (r,c) in visited:
                return 

            visited.add((r,c))

            if ind == (len(word) - 1):
                res = True

            backtrack(r + 1, c, ind +1)
            backtrack(r - 1, c, ind + 1)
            backtrack(r, c + 1, ind + 1)
            backtrack(r, c - 1, ind + 1)

            visited.remove((r,c))

        for i in range(ROW):
            for j in range(COL):
                backtrack(i, j, 0)

        return res 