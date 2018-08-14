class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 0
        characterIndex = {}
        start = 0
        end = 0
        for i, char in enumerate(s):
            if char in characterIndex:
                start = self.getNewStart(char, characterIndex)
            
            characterIndex[char] = i 
            length = end - start + 1
            print(start, end)
            maxLength = max(maxLength, length)
            end += 1
        return maxLength
            
    def getNewStart(self, char, characterIndex):
        #print(characterIndex)
        tempDic = characterIndex.copy()
        maxIndex = characterIndex[char] + 1
        for key in tempDic:
            if characterIndex[key] < maxIndex:
                del characterIndex[key]
        #print(characterIndex)
        return maxIndex
        