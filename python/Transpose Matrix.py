class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B = []
        
        for j in range(len(A[0])):
            B.append([])
            for i in range(len(A)):
                B[j].append(A[i][j])
                
        return B