class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        #Transpose of the matrix
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        #Mirror of the matrix
        for i in range(n //2):
            for j in range(n):
                matrix[j][i], matrix[j][n-i-1] = matrix[j][n-i-1],  matrix[j][i]
