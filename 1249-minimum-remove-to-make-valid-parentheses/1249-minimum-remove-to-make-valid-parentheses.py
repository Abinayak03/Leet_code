class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = []
        open_count = 0
        for ch in s:
            if ch == '(':
                open_count += 1

            elif ch == ')':
                if open_count == 0:
                    continue
                open_count -= 1

            result.append(ch)

        # Second pass only if unmatched opening parentheses exist
        if open_count > 0:
            final = []

            for ch in reversed(result):
                if ch == '(' and open_count > 0:
                    open_count -= 1
                    continue

                final.append(ch)

            return "".join(reversed(final))

        return "".join(result)