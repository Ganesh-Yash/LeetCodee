class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ra=len(arr1)
        for num1 in arr1:
            tr=0
            for num2 in arr2:
                if abs(num1-num2)<=d:
                    
                    if  tr==0:
                        ra-=1
                        tr=1
                    
        return ra
        