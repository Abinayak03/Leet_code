class Solution:
    def longestValidParentheses(self, s: str) -> int:
        open = 0
        close = 0
        max_len = 0

        for c in s:
            if c == '(':
                open+=1
            else:
                close+=1
            if open == close:
                max_len = max(max_len, 2*close)
            elif close>open:
                open = 0
                close = 0
        open = 0
        close = 0

        for c in reversed(s):
            if c == '(':
                open+=1
            else:
                close+=1
            if open == close:
                max_len = max(max_len, 2*close)
            elif close<open:
                open = 0
                close = 0
        return max_len
        
        '''stack = [-1]
        max_len = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i-stack[-1])
        return max_len'''