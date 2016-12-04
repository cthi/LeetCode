class Solution(object):

    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, key=lambda x: x[0])

        if not points:
            return 0

        amount = 1
        last = None

        for i in range(len(points)):
            if i == 0:
                last = points[i][1]
            else:
                if points[i][0] <= last:
                    last = min(last, points[i][1])
                else:
                    amount += 1
                    last = points[i][1]

        return amount
