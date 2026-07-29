from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        cnt = [0] * 26
        mid = ""

        for ch, f in freq.items():
            cnt[ord(ch) - ord('a')] = f // 2
            if f & 1:
                mid = ch

        LIMIT = k
        m = sum(cnt)

        def ways(count):
            """Number of distinct permutations of the multiset."""
            total = sum(count)
            res = 1
            rem = total
            for c in count:
                if c:
                    res *= comb(rem, c)
                    if res > LIMIT:
                        return LIMIT + 1
                    rem -= c
            return res

        if ways(cnt) < k:
            return ""

        left = []

        while m:
            for i in range(26):
                if cnt[i] == 0:
                    continue

                cnt[i] -= 1
                w = ways(cnt)

                if w >= k:
                    left.append(chr(i + ord('a')))
                    m -= 1
                    break
                else:
                    k -= w
                    cnt[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]
        