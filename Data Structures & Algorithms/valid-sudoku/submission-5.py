class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW = len(board)
        COL = len(board[0])

        for r in range(ROW):
            seen = set()
            for c in range(COL):
                cur = board[r][c]
                if cur == '.':
                    continue
                else:
                    if cur in seen:
                        return False
                    seen.add(cur)
        
        for c in range(COL):
            seen = set()
            for r in range(ROW):
                cur = board[r][c]
                if cur == '.':
                    continue
                else:
                    if cur in seen:
                        return False
                    seen.add(cur)
        
        r = 3
        c = 3
        while c < 10:
            while r < 10:
                seen = set()
                for i in range(r-3, r):
                    for j in range(c-3, c):
                        cur = board[i][j]
                        if cur == '.':
                            continue
                        else:
                            if cur in seen:
                                return False
                            seen.add(cur)
                r += 3
            c += 3
            r = 3
        return True
        
