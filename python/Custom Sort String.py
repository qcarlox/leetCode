class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        S = list(S)
        letterToVal = {}
        valToLetter = {}
        for i, char in enumerate(S):
            letterToVal[char] = i
            valToLetter[i] = char
            
        tMap = [] 
        for char in T:
            if char in letterToVal:
                tMap.append((char, letterToVal[char]))
            else:
                tMap.append((char, 26))
            
        
        tMap = sorted(tMap, key = lambda x: x[1] )
        sortedT = []
        for tup in tMap:
            sortedT.append(tup[0])
            
        return ''.join(sortedT)