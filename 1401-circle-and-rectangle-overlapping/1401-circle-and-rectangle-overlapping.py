class Solution:
    def checkOverlap(self, radius: int, xC: int, yC: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        cx=max(x1,min(xC,x2))
        cy=max(y1,min(yC,y2))
        dx=xC-cx
        dy=yC-cy
        return (dx**2 +dy**2)<=radius**2
        