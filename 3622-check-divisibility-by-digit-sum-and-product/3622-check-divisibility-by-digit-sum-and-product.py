class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x = n
        prod = 1
        sum = 0

        while n>0:
            rem = n%10
            prod*=rem
            sum+=rem

            n = n//10
        return x%(prod+sum)==0