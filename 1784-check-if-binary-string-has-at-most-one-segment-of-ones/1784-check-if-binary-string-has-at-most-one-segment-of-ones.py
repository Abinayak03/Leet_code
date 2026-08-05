class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        '''if s=="1":
            return True
        for i in range(1, len(s)-1):
            if s[i] == "1" and s[i-1] == "1":
                return True
        return False'''
        if '01' in s:
            return False
        else:
            return True