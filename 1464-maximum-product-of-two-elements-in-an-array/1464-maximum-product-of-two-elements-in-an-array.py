class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mi=1
        mii=1
        for i in nums:
            if mi<=i:
                mii=mi
                mi=i
            elif mii<=i:
                mii=i
        return (mi-1)*(mii-1)
        
      







        