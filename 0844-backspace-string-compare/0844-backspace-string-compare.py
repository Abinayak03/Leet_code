class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st_s = []
        st_t = []

        for c in s:
            if st_s and c == '#':
                st_s.pop()
            elif c!= '#':
                st_s.append(c)
        for c in t:
            if st_t and c == '#':
                st_t.pop()
            elif c!= '#':
                st_t.append(c)
        return st_s == st_t or st_s == st_t == []