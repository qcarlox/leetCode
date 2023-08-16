class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        digits = self.intToList(x)
        if x == 0:
            return x
        reversedNumber = self.listToReversedInt(digits)
        return reversedNumber
    
    def intToList(self, num):
        digits = []
        if num < 0:
            digits.append('-')
        num = abs(num)
        while num > 0:
            digits.append(num%10)
            num = num//10
        return digits
    
    def listToReversedInt(self, digits):
        negative = False
        if digits[0] == '-':
            negative = True
            del digits[0]
        
        num = 0
        for i, digit in enumerate(reversed(digits)):
            if (num > (2**31-1 - digit * 10**i) and not negative) or (num > (2**31 - digit * 10**i) and negative):
                return 0
            num += digit * 10**i
            
        if negative:
            return -1*num
        else:
            return num