pIGHT = 1
# DOWN = 2
# LEFT = 3

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        
        if not board:
            return 0
        
        N = len(board)
        M = len(board[0])
    
        battleships = 0
        shipLoc = set()
        
        for i in range(N):
            for j in range(M):
                if board[i][j] == 'X' and (i, j) not in shipLoc:
                    shipLoc.add((i, j))
                    battleships += 1
                    
                    self.floodShips(i - 1, j, 0, board, shipLoc, N, M)
                    self.floodShips(i, j + 1, 1, board, shipLoc, N, M)
                    self.floodShips(i + 1, j, 2, board, shipLoc, N, M)
                    self.floodShips(i, j - 1, 3, board, shipLoc, N, M)
        
        return battleships
        
    def floodShips(self, x, y, direction, board, shipLoc, N, M):
        if x < 0 or x >= N:
            return
        if y < 0 or y >= M:
            return
        
        if board[x][y] == 'X':
            shipLoc.add((x,y))
            
            if direction == 0:
                self.floodShips(x - 1, y, 0, board, shipLoc, N, M)
            elif direction == 1:
                self.floodShips(x, y + 1, 1, board, shipLoc, N, M)
            elif direction == 2:
                self.floodShips(x + 1, y, 2, board, shipLoc, N, M)
            else:
                self.floodShips(x, y - 1, 3, board, shipLoc, N, M)
        
