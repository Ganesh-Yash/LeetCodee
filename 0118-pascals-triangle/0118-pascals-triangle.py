class Solution:
    def generate(self, rs: int) -> List[List[int]]:
        tri=[]
        for i in range (rs):
            rows=[1]
            val=1
            for j in range (1,i+1):
                val=val*(i-j+1)//j
                rows.append(val)
            tri.append(rows)
        return tri




                


        