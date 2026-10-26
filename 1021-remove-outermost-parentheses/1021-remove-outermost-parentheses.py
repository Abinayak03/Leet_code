class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st = []
        bal = 0

        for c in s:
            if c == '(':
                if bal>0:
                    st.append(c)
                bal+=1
            else:
                bal-=1
                if bal>0:
                    st.append(c)
        return "".join(st)