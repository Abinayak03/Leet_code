class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        max_bar = 0
        stack = []

        for i in range(n+1):
            curr_height = 0 if i==n else heights[i]
            while stack and heights[stack[-1]] > curr_height:
                height = heights[stack.pop()]
                width = i if not stack else i-stack[-1]-1
                max_bar = max(max_bar, height*width)

            stack.append(i)
        return max_bar