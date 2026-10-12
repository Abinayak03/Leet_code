class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while stack and k>0 and int(stack[-1]) > int(c):
                stack.pop()
                k-=1
            stack.append(c)
        while k>0:
            stack.pop()
            k-=1
        
        while stack and stack[0] =='0':
            stack.pop(0)
        return "".join(stack if stack else "0")