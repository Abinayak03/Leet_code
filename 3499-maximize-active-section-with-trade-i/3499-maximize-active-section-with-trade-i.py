class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = "1" + s + "1"
        m = len(t)

        total = s.count("1")
        ans = total

        runs = []  # (char, length)
        i = 0
        while i < m:
            j = i
            while j < m and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j

        # runs alternate between 1 and 0
        # Look for: 0-run, 1-run, 0-run
        for i in range(1, len(runs) - 1):
            if (
                runs[i][0] == "1"
                and runs[i - 1][0] == "0"
                and runs[i + 1][0] == "0"
            ):
                left0 = runs[i - 1][1]
                one = runs[i][1]
                right0 = runs[i + 1][1]

                # subtract the artificial boundary 1's if included
                if i - 2 < 0:
                    left0 -= 1
                if i + 2 >= len(runs):
                    right0 -= 1

                gain = left0 + right0
                ans = max(ans, total + gain)

        return ans