class Solution(object):
    def totalNQueens(self, n):
        board = [['.' for i in range(n)] for j in range(n)]
        cols = [False for i in range(n)]
        
        return self.search(0, board, cols, n)
        
        
    def search(self, row, board, cols, n):
        if row == n:
            return 1
        
        ans = 0
        
        for i in range(n):
            if not cols[i] and self.validDiag(row, i, board, n):
                board[row][i] = 'Q'
                cols[i] = True
                
                ans += self.search(row + 1, board, cols, n)
                
                cols[i] = False
                board[row][i] = '.'
                
        return ans
                
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
