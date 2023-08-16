class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        morseCodeTranslations = set()
        for word in words:
            translatedWord = ''
            for char in word:
                translatedWord += morseCode[ord(char)-ord('a')]
            if translatedWord != '':
                morseCodeTranslations.add(translatedWord)
        return len(morseCodeTranslations)
                
        