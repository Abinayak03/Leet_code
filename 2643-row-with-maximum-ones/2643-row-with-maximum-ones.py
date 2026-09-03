class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        pos = 0
        count_1 = 0
        for i in range(m):
            count = 0
            for j in range(n):  
                if mat[i][j] == 1:
                    count += 1
            if count>count_1:
                count_1 = count
                pos = i
        return [pos, count_1]
                