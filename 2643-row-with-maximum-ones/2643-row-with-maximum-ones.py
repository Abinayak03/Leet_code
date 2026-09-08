class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        pos = 0
        count_1 = 0
        for i in range(m):
            count = sum(mat[i])
            if count>count_1:
                count_1 = count
                pos = i
        return [pos, count_1]
                