class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        def numAdjMine(board, r, c):
            mines = 0

            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue

                    if r + i >= 0 and r + \
                            i < len(board) and c + j >= 0 and c + j < len(board[0]) and board[r + i][c + j] == 'M':
                        mines += 1

            return mines

        def revealAdj(board, r, c):
            if r >= 0 and r < len(board) and c >= 0 and c < len(
                    board[0]) and board[r][c] == 'E':
                adjMines = numAdjMine(board, r, c)
                if adjMines == 0:
                    board[r][c] = 'B'

                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            revealAdj(board, r + i, c + j)
                else:
                    board[r][c] = str(adjMines)

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        else:
            revealAdj(board, click[0], click[1])

        return board
