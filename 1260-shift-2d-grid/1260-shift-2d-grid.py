class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * n for _ in range(m)]

        total = m * n
        k %= total

        for i in range(m):
            for j in range(n):

                # Flatten the matrix index.
                idx = i * n + j

                # New position after shift.
                nxt = (idx + k) % total

                ans[nxt // n][nxt % n] = grid[i][j]

        return ans


