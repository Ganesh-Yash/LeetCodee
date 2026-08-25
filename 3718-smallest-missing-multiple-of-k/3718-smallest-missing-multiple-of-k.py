class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        se=set()
        i=1
        while 1:
            if i*k not in nums:
                return i*k
            else:
                i+=1
        