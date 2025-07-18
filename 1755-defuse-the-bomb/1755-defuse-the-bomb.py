class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n

        for i in range(n):
            total = 0
            if k > 0:
                for j in range(1, k + 1):
                    total += code[(i + j) % n]
            elif k < 0:
                for j in range(1, abs(k) + 1):
                    total += code[(i - j + n) % n]
            res[i] = total

        return res