class Solution(object):

    def solveNQueens(self, n):
        ans = []
        board = [['.' for i in range(n)] for j in range(n)]
        cols = [False for i in range(n)]

        self.search(0, board, cols, ans, n)

        return ans

    def search(self, row, board, cols, ans, n):
        if row == n:
            ans.append([''.join(row) for row in board])
            return

        for i in range(n):
            if not cols[i] and self.validDiag(row, i, board, n):
                board[row][i] = 'Q'
                cols[i] = True

                self.search(row + 1, board, cols, ans, n)

                cols[i] = False
                board[row][i] = '.'

    def validDiag(self, row, col, board, n):
        origRow = row
        origCol = col

        while row >= 0 and col >= 0:
            if board[row][col] == 'Q':
                return False
            row -= 1
            col -= 1

        while origRow >= 0 and origCol < n:
            if board[origRow][origCol] == 'Q':
                return False
            origRow -= 1
            origCol += 1

        return True
