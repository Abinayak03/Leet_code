class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        word_len = len(word)
        count = 0
    
        for pattern in patterns:
            # Skip if pattern is longer than word
            if len(pattern) > word_len:
                continue
        
            if pattern in word:
                count += 1
    
        return count

        '''count = 0
        for pattern in patterns:
            if pattern in word:
                count+=1
        return count'''
