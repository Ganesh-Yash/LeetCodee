class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, j in enumerate(s, 1):
            ra = 26 - (ord(j) - ord('a'))
            total += ra * i
        return total