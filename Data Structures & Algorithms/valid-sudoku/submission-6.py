class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW = len(board)
        COL = len(board[0])

        for r in range(ROW):
            s = set()
            for c in range(COL):
                cur = board[r][c]
                if cur != '.':
                    if cur not in s:
                        s.add(cur)
                    else:
                        return False
        for c in range(COL):
            s = set()
            for r in range(ROW):
                cur = board[r][c]
                if cur != '.':
                    if cur in s:
                        return False
                    s.add(cur)
        
        r = 3
        c = 3
        while r < 10:
            while c < 10:
                s = set()
                for i in range(r-3, r):
                    for j in range(c-3, c):
                        cur = board[i][j]
                        if cur != '.':
                            if cur in s:
                                return False
                            s.add(cur)
                c += 3
            r += 3
            c = 3
        return True
                        
