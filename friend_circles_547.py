class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        seen = [False for i in range(N)]
        groups = 0

        for i in range(N):
            if not seen[i]:
                groups += 1
                self.flood_fill(i, seen, M, N)

        return groups

    def flood_fill(self, i, seen, M, N):
        seen[i] = True

        for j in range(N):
            if M[i][j] and not seen[j]:
                self.flood_fill(j, seen, M, N)
