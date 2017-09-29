class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def newState(board, c, r, M, N):
            aliveCells = 0

            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (not (i == 0 and j == 0)) and c + i >= 0 and r + \
                            j >= 0 and c + i < M and r + j < N:
                        aliveCells += board[c + i][r + j] & 1

            if not board[c][r] & 1:
                return 2 if aliveCells == 3 else board[c][r]
            else:
                return 3 if 2 <= aliveCells <= 3 else board[c][r]

        M = len(board)
        N = len(board[0])

        for i in range(M):
            for j in range(N):
                board[i][j] = newState(board, i, j, M, N)

        for i in range(M):
            for j in range(N):
                board[i][j] = board[i][j] >> 1
