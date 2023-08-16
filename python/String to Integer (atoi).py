class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        number = 0
        sign = 1
        index = 0
        while index < len(s):
            character = s[index]
            if character == ' ':
                index += 1
                continue
            elif character == '-':
                index += 1
                sign = -1
                break
            elif character == '+':
                index += 1
                sign = 1
                break
            elif (character >= '0' and character <= '9'):
                break
            else:
                return 0
                
                
        for i in range(index, len(s)):
            character = s[i]
            print(character)
            if not (character >= '0' and character <= '9'):
                break
            elif sign == 1:
                digit = ord(s[i])-ord('0')
                number = self.multiplyWithOverflow(number, 10, 2**31-1)
                number = self.addWithOverflow(number, digit, 2**31-1)
            elif sign == -1:
                digit = ord(s[i])-ord('0')
                number = self.multiplyWithOverflow(number, 10, 2**31)
                number = self.addWithOverflow(number, digit, 2**31)
            
        return number*sign
    
    def addWithOverflow(self, a, b, maxVal):
        if a > maxVal-b:
            return maxVal
        else:
            return a + b

    def multiplyWithOverflow(self, a, b, maxVal):
        if a > maxVal/b:
            return maxVal
        else:
            return a * b
            
            