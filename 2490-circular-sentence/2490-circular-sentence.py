class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        n = len(words)

        if n==1:
            if words[0][0] == words[0][-1]:
                return True
        
        if words[0][0] == words[-1][-1]:
            for i in range(1, n):
                if words[i][0] != words[i-1][-1]:
                    return False
            return True
        return False