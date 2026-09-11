class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        #seen = {}
        seen = set()

        for i in range(n):
            if digits[i] == 0:
                continue

            for j in range(n):
                if j == i:
                    continue

                for k in range(n):
                    if k==i or k==j or digits[k] %2 != 0:
                        continue
                    x = digits[i]*100 + digits[j]*10 + digits[k]
                    #seen[x] = True
                    seen.add(x)
        return len(seen)
                