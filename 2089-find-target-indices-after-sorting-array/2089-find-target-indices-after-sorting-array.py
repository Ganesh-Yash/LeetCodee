class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        tr=[]
        nums.sort()
        for i in range (len(nums)):
            if nums[i]==target:
                tr.append(i)
        return tr
        