class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        col = 0

        while l <= r:
            mid  = l + (r-l)//2

            if target == matrix[mid][0]:
                return True
            
            if target < matrix[mid][0]:
                r = mid - 1
            
            elif target > matrix[mid][0]:
                l = mid + 1
        row = r
        
        l1 = 0
        r1 = len(matrix[0]) - 1

        while l1 <= r1:
            mid  = l1 + (r1-l1)//2

            if target == matrix[row][mid]:
                return True
            
            if target < matrix[row][mid]:
                r1 = mid - 1
            
            elif target > matrix[row][mid]:
                l1 = mid + 1

        return False
                