class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def exists_h(board, used, r, c, word, pos):
            if pos == len(word):
                return True
            elif r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
                return False
            elif used[r][c]:
                return False
            elif board[r][c] == word[pos]:
                used[r][c] = True

                for dir in dirs:
                    if exists_h(
                            board,
                            used,
                            r + dir[0],
                            c + dir[1],
                            word,
                            pos + 1):
                        return True

                used[r][c] = False

            return False

        used = [[False for c in range(len(board[0]))]
                for r in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if exists_h(board, used, i, j, word, 0):
                    return True

        return False
