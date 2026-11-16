class Solution:
    def digitSum(self, s: str, k: int) -> str:
        n = len(s)
        while n>k:
            temp = []
            for i in range(0,len(s),k):
                val = 0
                for j in range(i, min(i+k, len(s))):
                    val+=int(s[j])
                temp.append(str(val))
            s = "".join(temp)
            n=len(s)
        return s