class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
                
        for row in range(len(A)):
            score, invertedScore = self.scoreRow(row, A)
            if score < invertedScore:
                self.toggleRow(row, A)
                
        for column in range(len(A[0])):
            score, invertedScore = self.scoreColumn(column, A)
            if score < invertedScore:
                self.toggleColumn(column, A)

        totalScore = 0
        for row in range(len(A)):
            score, invertedScore = self.scoreRow(row, A)
            if score < invertedScore:
                totalScore += invertedScore
            else:
                totalScore += score
        
        return totalScore
        
        
    def toggleRow(self, row, A):
        for column in range(len(A[0])):
            A[row][column] = 1-A[row][column]
        return
    
    def toggleColumn(self, column, A):
        for row in range(len(A)):
            A[row][column] = 1-A[row][column]
        return
    
    def scoreColumn(self, column, A):
        score = 0
        invertedScore = 0
        for row in range(len(A)):
            score += A[row][column]
            invertedScore += 1-A[row][column]
        return score, invertedScore
    
    def scoreRow(self, row, A):
        score = 0
        invertedScore = 0
        for column in range(len(A[0])):
            value = A[row][len(A[0])-column-1]
            score += value*2**(column)
            invertedScore += (1-value)*2**(column)
        return score, invertedScore
        