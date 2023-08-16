class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        differentBits = x ^ y
        
        count = 0
        while differentBits != 0:
            if(differentBits % 2 == 1):
                count += 1
            differentBits //= 2
        return count