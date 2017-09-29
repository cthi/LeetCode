class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        M = len(board)
        N = len(board[0])

        Q = []

        for i in range(M):
            Q.append((i, 0))
            Q.append((i, N - 1))

        for i in range(N):
            Q.append((M - 1, i))
            Q.append((0, i))

        while Q:
            i, j = Q.pop(0)
            if 0 <= i < M and 0 <= j < N and board[i][j] == 'O':
                board[i][j] = 'Z'

                Q.append((i + 1, j))
                Q.append((i - 1, j))
                Q.append((i, j + 1))
                Q.append((i, j - 1))

        for i in range(M):
            for j in range(N):
                if board[i][j] == 'Z':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
