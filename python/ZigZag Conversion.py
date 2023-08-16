class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        numRows = min(numRows, len(s))
        rows = []
        for i in range(numRows):
            rows.append([])
            
        offset = 1
        rowIndex = 0
        for character in s:
            rows[rowIndex].append(character)
            if rowIndex == numRows-1:
                offset = -1
            if rowIndex == 0:
                offset = 1
            
            rowIndex += offset
        
        zigZagString = ""
        for row in rows:
            zigZagString += ''.join(row)
        return zigZagString
            