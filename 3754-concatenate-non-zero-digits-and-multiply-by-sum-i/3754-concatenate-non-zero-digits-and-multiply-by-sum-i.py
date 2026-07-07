class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ""
        sum = 0
         
        for i in str(n):
            if i!="0":
                x+=i
            sum += int(i)
            if x == "":
                return 0
            
        return int(x) * sum
