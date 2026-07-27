class Solution:
    def maxArea(self, h: List[int]) -> int:
        mx=float('-inf')
        i=0
        j=len(h)-1
        while i<j:
            mx=max(mx,min(h[i],h[j])*(j-i))
            if h[j]<h[i]:
                j-=1
            else:
                i+=1
        return mx



        