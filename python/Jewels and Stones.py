class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = set()
        for j in J:
            jewels.add(j)
            
        numberOfJewels = 0
        for s in S:
            if s in jewels:
                numberOfJewels += 1
                
        return numberOfJewels