class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
        '''sum_odd = 0
        sum_even = 0
        for o in range(1, 2*n+1, 2):
            sum_odd+=o
        for e in range(2, 2*n+1, 2):
            sum_even+=e
        return math.gcd(sum_odd, sum_even)'''
