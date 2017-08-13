class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        p = [0, 0]

        for move in moves:
            if move == 'R':
                p[0] += 1
            elif move == 'L':
                p[0] -= 1
            elif move == 'U':
                p[1] += 1
            else:
                p[1] -= 1

        return p == [0, 0]
