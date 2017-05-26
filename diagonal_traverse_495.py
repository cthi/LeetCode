class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix

        N = len(matrix)
        M = len(matrix[0])
        output = []

        for i in range(N):
            c = i
            j = 0
            tmp = []

            while c > -1 and j < M:
                tmp.append(matrix[c][j])
                c -= 1
                j += 1

            if i % 2 == 1:
                output.extend(reversed(tmp))
            else:
                output.extend(tmp)

        for j in range(1, M):
            c = j
            i = N - 1
            tmp = []

            while c < M and i > -1:
                tmp.append(matrix[i][c])
                c += 1
                i -= 1

            if N % 2 == 0:
                if j % 2 == 1:
                    output.extend(tmp)
                else:
                    output.extend(reversed(tmp))
            else:
                if j % 2 == 1:
                    output.extend(reversed(tmp))
                else:
                    output.extend(tmp)

        return output
