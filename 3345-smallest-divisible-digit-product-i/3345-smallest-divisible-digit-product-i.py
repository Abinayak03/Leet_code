class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        if n%10 == 0:
            return n
        elif t==1:
            return n
        else:
            for i in range(n, n + 10):
                if reduce(mul, map(int,str(i))) %t == 0: return i



