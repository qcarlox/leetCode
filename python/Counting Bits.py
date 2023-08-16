class Solution:
    import math
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        counts = [0]
        for i in range(1, num+1):
            if i%2 == 0:
                counts.append(counts[i//2])
            else:
                counts.append(counts[i-1]+1)
        return counts