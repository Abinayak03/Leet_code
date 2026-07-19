class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {}

        # Last occurrence of every character
        for i, ch in enumerate(s):
            last[ch] = i

        stack = []
        visited = set()

        for i, ch in enumerate(s):

            # Skip if already included
            if ch in visited:
                continue

            # Remove larger characters that appear later
            while (stack and
                   stack[-1] > ch and
                   last[stack[-1]] > i):
                visited.remove(stack.pop())

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)