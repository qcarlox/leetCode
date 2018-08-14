class Solution:
    def toLowerCase(self, string):
        """
        :type str: str
        :rtype: str
        """
        string = list(string)
        for i, c in enumerate(string):
            if (c >= 'a' and c <= 'z'):
                continue
            elif (c >= 'A' and c <= 'Z'):
                string[i] = chr(ord(c) - ord('A') + ord('a'))
        return ''.join(string)