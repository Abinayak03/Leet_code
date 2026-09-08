class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        startCol = 0
        endCol = len(mat[0]) - 1

        while startCol <= endCol:

            # Find the middle column.
            midCol = (startCol + endCol) // 2

            # Find the maximum element in the middle column.
            maxRow = self.findMaxRow(mat, midCol)

            currentValue = mat[maxRow][midCol]

            # Check if the left neighbor is bigger.
            if midCol > 0:
                if mat[maxRow][midCol - 1] > currentValue:
                    endCol = midCol - 1
                    continue

            # Check if the right neighbor is bigger.
            if midCol < len(mat[0]) - 1:
                if mat[maxRow][midCol + 1] > currentValue:
                    startCol = midCol + 1
                    continue

            # Neither left nor right is bigger,
            # so the current element is a peak.
            return [maxRow, midCol]

        return []

    def findMaxRow(self, mat, col):
        maxRow = 0

        for row in range(len(mat)):
            if mat[row][col] > mat[maxRow][col]:
                maxRow = row

        return maxRow