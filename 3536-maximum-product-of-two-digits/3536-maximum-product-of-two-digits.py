class Solution:
    def maxProduct(self, n: int) -> int:
        str_n = str(n)
        list_n = list(str_n)
        list_n.sort()
        return int(list_n[-1])*int(list_n[-2])