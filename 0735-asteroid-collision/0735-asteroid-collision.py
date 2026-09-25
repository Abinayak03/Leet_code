class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            while stack and stack[-1]>0 and a<0 and stack[-1] < -a:
                stack.pop()
            if stack and stack[-1]>0 and a<0:
                if stack[-1] == -a:
                    stack.pop()
            else:
                stack.append(a)
        return stack