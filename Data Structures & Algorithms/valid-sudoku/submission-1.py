class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            seen = set()
            for i in range(len(board[0])):
                # print(board[row][i])
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False 
                seen.add(board[row][i])
        
        for col in range(len(board[0])):
            seen = set()
            for i in range(len(board)):
                cur = (board[i][col])
                if cur == ".":
                    continue
                if cur in seen:
                    return False
                seen.add(cur)
        
        r = 3
        c = 3
        while c < 10:
            while r < 10:
                seen = set()
                for i in range(r-3,r):
                    for j in range(c-3, c):
                        cur = board[i][j]
                        if cur == ".":
                            continue
                        if cur in seen:
                            return False
                        seen.add(cur)
                r += 3
            c += 3
            r = 3
        
        return True
            

                