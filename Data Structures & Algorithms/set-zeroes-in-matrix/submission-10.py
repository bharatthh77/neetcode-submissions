class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROW = len(matrix)
        COL = len(matrix[0])
        col_0 = False

        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0:
                    if c != 0:
                        matrix[0][c] = 0
                        matrix[r][0] = 0
                    else:
                        col_0 = True
                        matrix[r][0] = 0
        
        for i in range(1, ROW):
            for j in range(1, COL):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(COL):
                matrix[0][i] = 0

        if col_0:
            for i in range(ROW):
                matrix[i][0] = 0
        



        
        