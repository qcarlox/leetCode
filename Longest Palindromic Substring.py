class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        evenPalindromes = self.scanStringUsingWindow(s, 2)
        oddPalindromes = self.scanStringUsingWindow(s, 3)
        longestSubstring = ''
        #print(evenPalindromes)
        if len(s) > 0:
            longestSubstring = s[0]
        
        if len(evenPalindromes) != 0:
            longestSubstring = list(evenPalindromes.keys())[0]
                
        if len(oddPalindromes) != 0:
            longestSubstring = list(oddPalindromes.keys())[0]
            
        while len(evenPalindromes) != 0:
            evenPalindromes = self.expandPalindromes(evenPalindromes, s)
            #print(evenPalindromes)
            if len(evenPalindromes) != 0:
                longestSubstring = list(evenPalindromes.keys())[0]
            
        while len(oddPalindromes) != 0:
            oddPalindromes = self.expandPalindromes(oddPalindromes, s)
            if len(oddPalindromes) != 0:
                longestOddSubstring = list(oddPalindromes.keys())[0]
                
                if len(longestOddSubstring) > len(longestSubstring):
                    longestSubstring = longestOddSubstring
        return longestSubstring
        
    def expandPalindromes(self, palindromeDictionary, s):
        tempDic = {}    
        for substring in palindromeDictionary:
            startList = palindromeDictionary[substring]
            for i in startList:
                start = i-1
                end = start+len(substring)+1
                #print("start: " + str(start))
                #print("end: " + str(end))
                if(end < len(s) and start >= 0):
                    if(s[start] == s[end]):
                        newSubstring = s[start:end+1]
                        #print(newSubstring)
                        if newSubstring in tempDic:
                            tempDic[newSubstring].append(start)
                        else:
                            tempDic[newSubstring] = [start]
        return tempDic
                 
        
    def scanStringUsingWindow(self, s, windowLength):
        start = 0
        end = start+windowLength
        palindromeDictionary = {}
        while end <= len(s):
            substring = s[start:end]
            if self.isPalindrome(substring):
                if substring in palindromeDictionary:
                    palindromeDictionary[substring].append(start)
                else:
                    palindromeDictionary[substring] = [start]
            start += 1
            end += 1
        return palindromeDictionary
        
    def isPalindrome(self, substring):
        end = len(substring)
        for i in range(end//2):
            if(substring[i] != substring[end-1-i]):
                return False
        return True
        