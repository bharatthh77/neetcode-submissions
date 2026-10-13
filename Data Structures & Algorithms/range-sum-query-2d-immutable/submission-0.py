class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROW = len(matrix)
        COL = len(matrix[0])

        self.pCopy = [[0]*(COL + 1) for r in range(ROW +1)]

        for i in range(1, ROW + 1):
            prefix = 0
            for j in range(1, COL + 1):
                prefix += matrix[i - 1][j - 1]
                self.pCopy[i][j] = prefix + self.pCopy[i-1][j]
            

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1 = row1 + 1, col1 + 1
        row2, col2 = row2 + 1, col2 + 1

        res = self.pCopy[row2][col2]

        res -= self.pCopy[row1 -1][col2]
        res -= self.pCopy[row2][col1 -1]
        res += self.pCopy[row1 - 1][col1 -1]

        return res



        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)