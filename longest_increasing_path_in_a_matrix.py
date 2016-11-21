class Solution(object):

    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0

        N = len(matrix)
        M = len(matrix[0])

        dp = [[None for i in range(M)] for j in range(N)]
        seen = [[False for i in range(M)] for j in range(N)]

        ans = 0

        for row in range(N):
            for col in range(M):
                ans = max(
                    ans,
                    self.search(
                        float('-inf'),
                        row,
                        col,
                        matrix,
                        dp,
                        seen,
                        N,
                        M))

        return ans

    def search(self, last, row, col, matrix, dp, seen, N, M):
        if row == N or row < 0 or col == M or col < 0:
            return 0

        if seen[row][col]:
            return 0
        else:
            seen[row][col] = True

        if matrix[row][col] <= last:
            seen[row][col] = False
            return 0

        if dp[row][col]:
            seen[row][col] = False
            return dp[row][col]

        lens = []

        lens.append(
            self.search(
                matrix[row][col],
                row + 1,
                col,
                matrix,
                dp,
                seen,
                N,
                M))
        lens.append(
            self.search(
                matrix[row][col],
                row - 1,
                col,
                matrix,
                dp,
                seen,
                N,
                M))
        lens.append(
            self.search(
                matrix[row][col],
                row,
                col + 1,
                matrix,
                dp,
                seen,
                N,
                M))
        lens.append(
            self.search(
                matrix[row][col],
                row,
                col - 1,
                matrix,
                dp,
                seen,
                N,
                M))

        res = 1 + max(lens)
        dp[row][col] = res
        seen[row][col] = False

        return res
