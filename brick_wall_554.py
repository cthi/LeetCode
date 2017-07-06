from collections import Counter


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        counter = Counter()

        for row in wall:
            gapLoc = 0

            for gap in row[:len(row) - 1]:
                gapLoc += gap
                counter[gapLoc] += 1

        if not counter:
            return len(wall)

        return len(wall) - counter.most_common(1)[0][1]
