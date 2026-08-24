class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        high = row-1
        low = 0
        target_row = -1

        while low<=high:
            mid = (low + high)//2
            if matrix[mid][0] <= target and matrix[mid][col-1] >= target:
                target_row = mid
                break
            elif matrix[mid][0] > target:
                high = mid-1
            else:
                low = mid+1
        
        if target_row == -1:
            return False
        
        low = 0
        high = col-1

        while low <= high:
            mid = (low + high)//2
            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] > target:
                high = mid-1
            else:
                low = mid+1
        
        return False