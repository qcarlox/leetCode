class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        listOfSets = []
        for char in S:
            newLetter = True
            setsToMergeIndex = []
            for i, charSet in enumerate(listOfSets):
                if char in charSet:
                    newLetter = False
                    setsToMergeIndex.append(i)
                    break
                    
            if newLetter == True:
                newSet = set(char)
                listOfSets.append(newSet)
            else:
                start = setsToMergeIndex[0]
                end = len(listOfSets)
                newSet = set()
                for i in range(start, end):
                    setToAdd = listOfSets[i]
                    newSet = newSet.union(setToAdd)
                listOfSets = listOfSets[0:start] + [newSet]
        
        listOfLengths = [0]*len(listOfSets)
        for char in S:
            for i, charSet in enumerate(listOfSets):
                if char in charSet:
                    listOfLengths[i] += 1
                    break
                    
        return listOfLengths
                    
                