class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        used = [False for i in range(N)]
        return self.countArrangement_h(N, 1, used)

    def countArrangement_h(self, N, pos, used):
        if pos == N + 1:
            return 1

        ways = 0

        for index, u in enumerate(used):
            if not u and ((index + 1) % pos == 0 or pos % (index + 1) == 0):
                used[index] = True
                ways += self.countArrangement_h(N, pos + 1, used)
                used[index] = False

        return ways
