class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict

        types = defaultdict(int)
        left = 0
        max_len = 0

        for r in range(len(fruits)):
            types[fruits[r]]+=1

            while len(types)>2:
                types[fruits[left]]-=1
                if types[fruits[left]]==0:
                    del types[fruits[left]]
                left+=1
            max_len = max(max_len, r-left+1)
        return max_len
