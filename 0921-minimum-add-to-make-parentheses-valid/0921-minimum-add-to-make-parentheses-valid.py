class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        '''stack = []

        for c in s:
            if stack and c == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
        return len(stack)'''

        open = 0
        close = 0
        for c in s:
            if c == '(':
                open+=1
            else:
                if open>0:
                    open-=1
                else:
                    close+=1
        return open+close

        