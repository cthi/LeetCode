class Solution(object):

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        M = matrix
        N = len(M)
        S = 0
        E = N - 1
        row = 0

        while S < E:
            for col in range(S, E):
                c, d = (col, N - row - 1)
                e, f = (d, N - c - 1)
                g, h = (f, N - e - 1)

                M[row][col], M[c][d], M[e][f], M[g][h] = M[
                    g][h], M[row][col], M[c][d], M[e][f]

            row += 1
            S += 1
            E -= 1
