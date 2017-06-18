class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        timePoints = sorted([self.asHr(x) for x in timePoints])
        diffs = []

        for i in range(len(timePoints) - 1):
            diffs.append(timePoints[i + 1] - timePoints[i])

        diffs.append(timePoints[0] + 1440 - timePoints[-1])
        return min(diffs)

    def asHr(self, pt):
        hr = int(pt[:2])
        mins = int(pt[3:])

        return 60 * hr + mins
