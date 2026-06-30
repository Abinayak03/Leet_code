class Solution:
    from collections import defaultdict

    def numberOfSubstrings(self, s: str) -> int:
        freq = defaultdict(int)
        left = 0
        count = 0
        n = len(s)

        for right in range(n):
            freq[s[right]] += 1

            while len(freq) == 3:
                count += (n - right)

                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]

                left += 1

        return count