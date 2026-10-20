class Solution:
    def climbStairs(self, n: int) -> int:
        '''if n<=2: return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)'''
        if n<=2: 
            return n
        n1 = 1
        n2 = 2
        for i in range(3, n+1):
            n3 = n1+n2
            temp = n3
            n1 = n2
            n2 = temp
        return n3