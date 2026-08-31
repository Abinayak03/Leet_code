class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        m = 0
        n = col-1

        while m<row and n>=0:
            if matrix[m][n] == target:
                return True
            elif matrix[m][n] > target:
                n -= 1
            else:
                m+=1
        return False