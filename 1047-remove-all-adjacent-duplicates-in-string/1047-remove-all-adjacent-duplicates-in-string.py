class Solution:
    def removeDuplicates(self, s: str) -> str:
        st=[]
        st.append("")
        for i in s:
            if st[-1]!=i:
                st.append(i)
            else:
                st.pop()
        return "".join(st)
        