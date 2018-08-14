# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) == 1:
            return 1
        maxPoints = 0
        for firstPoint in points:
            slopeCount = {}
            for secondPoint in points:
                if firstPoint == secondPoint:
                    slope = 'dup'
                elif ((firstPoint.x-secondPoint.x) == 0) and ((firstPoint.y-secondPoint.y) != 0):
                    slope = 'inf'
                elif ((firstPoint.x-secondPoint.x) == 0) and ((firstPoint.y-secondPoint.y) == 0):
                    slope = 'dup'
                else:
                    xDif = (firstPoint.x-secondPoint.x)
                    yDif = (firstPoint.y-secondPoint.y)
                    div = self.gcd(yDif, xDif)
                    xDif //= div
                    yDif //= div
                    slope = (xDif, yDif)
                    
                if slope in slopeCount:
                    slopeCount[slope] += 1
                else:
                    slopeCount[slope] = 1

            for slope in slopeCount:
                if slope != 'dup':
                    maxPoints = max(slopeCount[slope] + slopeCount['dup'], maxPoints)
                else:
                    maxPoints = max(slopeCount[slope], maxPoints)
        return maxPoints

    def gcd(self, m, n):          
        while (n != 0):
            r = m % n      
            m = n            
            n = r     
        return m;      