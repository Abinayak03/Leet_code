class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        res = [0] * n

        l = 0
        curr_sum = 0
        for r in range(n + abs(k)):
            curr_sum += code[r %n ]
            if (r-l+1) > abs(k):
                curr_sum -= code[l%n]
                l = (l+1)%n
            
            if (r-l+1) == abs(k):
                if k>0:
                    res[(l-1)%n] = curr_sum
                elif k<0:
                    res[(r+1)%n] = curr_sum
        return res