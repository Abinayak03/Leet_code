class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        rows = len(matrix)
        columns = len(matrix[0])
        heights = [0]*columns
        max_score = 0

        for r in range(rows):
            for c in range(columns):
                if matrix[r][c] == '1':
                    heights[c]+=1
                else:
                    heights[c] = 0
            max_score = max(max_score, self.calc_max_score(heights))
        return max_score

    def calc_max_score(self, heights):
        n = len(heights)
        max_score = 0
        stack = []

        for i in range(n+1):
            curr_height = 0 if i==n else heights[i]
            while stack and heights[stack[-1]] > curr_height:
                height = heights[stack.pop()]
                width = i if not stack else i-stack[-1]-1
                max_score = max(max_score, height*width)
            stack.append(i)

        return max_score
