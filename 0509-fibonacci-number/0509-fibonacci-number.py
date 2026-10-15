class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n

        #recursive code
        return self.fib(n-1) + self.fib(n-2)

        '''n1 = 0
        n2 = 1

        for i in range(2, n+1):
            n3 = n1+n2
            temp = n3
            n1 = n2
            n2 = temp
        return n3'''