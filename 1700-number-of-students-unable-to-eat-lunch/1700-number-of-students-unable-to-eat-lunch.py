class Solution:
    def countStudents(self, st: List[int], sd: List[int]) -> int:
        ct = 0
        while len(st) > ct:
            if st[0] == sd[0]:
                sd.pop(0)
                ct = 0
            else:
                st.append(st[0])
                ct+=1

            st.pop(0)
        return len(st)
		
#Upvote will be encouraging.