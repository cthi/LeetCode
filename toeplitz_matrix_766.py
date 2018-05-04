class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        N = len(matrix)
        M = len(matrix[0])
        
        for i in range(1, N):
            for j in range(1, M):
                if matrix[i - 1][j - 1] != matrix[i][j]:
                    return False
        return True
