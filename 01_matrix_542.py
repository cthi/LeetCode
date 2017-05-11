class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        N = len(matrix)
        M = len(matrix[0])

        output = [[-1 for i in range(M)] for i in range(N)]

        Q = []

        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    output[i][j] = 0
                    Q.append((i, j))

        c = 1

        while Q:
            children = []

            for node in Q:
                i = node[0]
                j = node[1]

                if i + 1 < N:
                    if output[i + 1][j] == -1:
                        output[i + 1][j] = c
                        children.append((i + 1, j))

                if i - 1 > -1:
                    if output[i - 1][j] == -1:
                        output[i - 1][j] = c
                        children.append((i - 1, j))

                if j + 1 < M:
                    if output[i][j + 1] == -1:
                        output[i][j + 1] = c
                        children.append((i, j + 1))

                if j - 1 > -1:
                    if output[i][j - 1] == -1:
                        output[i][j - 1] = c
                        children.append((i, j - 1))

            c += 1
            Q = children
            children = []

        return output
