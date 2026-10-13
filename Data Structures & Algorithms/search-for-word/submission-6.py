import copy
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        ROW = len(board)
        COL = len(board[0])
        copy_board = copy.deepcopy(board)
        
        def backtrack(index, row, col):
            nonlocal res
            nonlocal copy_board

            # print(board)

            # print('copy: ', copy_board)

            # print('index: ', index)

            # print('board row, col', row, col, res)
            if res or len(word) - 1 < index:
                return

            if (ROW -1 < row) or (COL - 1 < col) or row < 0 or col < 0 or board[row][col] != word[index] or board[row][col] == '#':
                return

            if len(word) - 1 == index and board[row][col] == word[-1]:
                res = True
                return


            if board[row][col] == word[index]:
                board[row][col] = '#'
            
            
            backtrack(index + 1, row - 1, col)
            # if (ROW > row-1) and (COL > col) and row -1 >= 0 or col >= 0:
            #     board[row-1][col] = copy_board[row-1][col]

            backtrack(index + 1, row, col + 1)
            # if (ROW > row) and (COL > col+1) and row >= 0 or col+1 >= 0:    
            #     board[row][col+1] = copy_board[row][col+1]
            
            backtrack(index + 1, row + 1, col)
            # if (ROW > row+1) and (COL > col) and row +1 >= 0 or col >= 0:
            #     board[row+1][col] = copy_board[row+1][col]

            backtrack(index + 1, row, col -1)
            # if (ROW > row) and (COL > col-1) and row >= 0 or col-1 >= 0:
            #     board[row][col-1] = copy_board[row][col-1]
            board[row][col] = copy_board[row][col]
                
        
        for i in range(ROW):
            for j in range(COL):
                backtrack(0, i, j)

        return res
