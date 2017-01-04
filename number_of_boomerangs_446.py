import math


class Solution(object):

    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        N = len(points)
        H = [{} for i in range(N)]

        for i in range(N):
            x = points[i]
            for j in range(i + 1, N):
                y = points[j]
                ans = math.hypot(x[0] - y[0], x[1] - y[1])

                if ans in H[i]:
                    H[i][ans] += 1
                else:
                    H[i][ans] = 1

                if ans in H[j]:
                    H[j][ans] += 1
                else:
                    H[j][ans] = 1

        ans = 0

        for ht in H:
            for k, v in ht.items():
                if v >= 2:
                    ans += v * (v - 1)

        return ans
