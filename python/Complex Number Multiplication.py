class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        aReal = int(a[0:a.index('+')])
        aImaginary = int(a[a.index('+')+1:a.index('i')])
        
        
        bReal = int(b[0:b.index('+')])
        bImaginary = int(b[b.index('+')+1:b.index('i')])

        cReal = aReal*bReal - aImaginary*bImaginary
        cImaginary = aReal*bImaginary + aImaginary*bReal
        
        return str(cReal) + '+' + str(cImaginary) + 'i'