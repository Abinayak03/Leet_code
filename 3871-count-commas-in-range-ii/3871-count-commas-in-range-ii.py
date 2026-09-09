class Solution:
    def countCommas(self, n: int) -> int:
        commas = 0
        start = 1000

        while start<=n:
            commas += n-start+1
            start *= 1000
        return commas
