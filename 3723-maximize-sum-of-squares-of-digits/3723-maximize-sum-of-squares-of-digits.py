'''class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        good = -1
        ans = ""

        for i in range(sum + 1):
            for j in range(sum, -1, -1):
                g = i*i + j*j
                current = str(i) + str(j)
                if i + j == sum and len(current) == num:
                    if g > good or (g == good and current > ans):
                        good = g
                        ans = str(i) + str(j)

        return ans'''

class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        q, r = divmod(sum, 9)

        res = ("9" * q) + (str(r) * (r > 0)) + ("0" * (num - q - (r > 0)))
        return res
