class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        leng = 0
        for s in sentences:
            leng = max(leng, len(s.split(" ")))
        return leng