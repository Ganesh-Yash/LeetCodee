class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix),len(matrix[0])
        zr,zs=set(),set()
        for i in range (m):
            for j in range (n):
                if matrix[i][j]==0:
                    zr.add(i)
                    zs.add(j)
        for i in zr:
            matrix[i]=[0]*n
        for j in zs:
            for i in range (m):
                matrix[i][j]=0
        return matrix


        