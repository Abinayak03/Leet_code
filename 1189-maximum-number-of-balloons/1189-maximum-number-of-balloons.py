class Solution:
    from collections import defaultdict
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = defaultdict(int)

        for t in text:
            if t in "balloon":
                hashmap[t] += 1

        if len(hashmap) == 5 and hashmap['l'] >=2 and hashmap['o'] >= 2:
            return min(hashmap['b'],
                hashmap['a'],
                hashmap['l'] // 2,
                hashmap['o'] // 2,
                hashmap['n'])
        else:
            return 0