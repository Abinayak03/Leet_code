class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        n = len(mat)

        low = mat[0][0]
        high = mat[n - 1][n - 1]
        ans = low
        while low<=high:
            mid = (low+high)//2
            if self.countLessEqual(mat, n, mid, k):
                ans = mid
                high = mid-1
            else:
                low = mid+1

        return ans

    def countLessEqual(self, mat: List[List[int]], n: int, target: int, k: int) -> bool:
        row = n - 1
        col = 0
        count = 0

        while row >= 0 and col < n:
            if mat[row][col] <= target:
                count += row + 1
                col += 1
            else:
                row -= 1

        return count >= k
"""We use >= k instead of == k because the matrix can contain duplicate values. For example, if the sorted elements are [1, 2, 2, 2] and k = 2, the 2nd smallest element is 2, but there are actually 4 elements less than or equal to 2. So count == k would fail, whereas count >= k correctly identifies 2 as the answer."""