class Solution:
    def calPoints(self, operations: List[str]) -> int:
        yy=[]
        for i in operations:
    
              
            if i=="+":
                yy.append(yy[-1]+yy[-2])
            elif i=="D":
                yy.append(2*yy[-1])
            elif i=="C":
                yy.pop()
            else:
                yy.append(int(i))
        return sum(yy)
        