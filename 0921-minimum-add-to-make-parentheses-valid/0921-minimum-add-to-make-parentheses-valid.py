class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for c in s:
            if stack and c == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
        return len(stack)