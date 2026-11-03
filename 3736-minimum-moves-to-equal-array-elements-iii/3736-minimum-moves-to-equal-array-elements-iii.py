class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mi=max(nums)
        return sum(mi-num for num in nums)
        