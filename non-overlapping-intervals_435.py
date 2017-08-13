# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals = sorted(intervals, key=lambda x: x.start)
        removed = 0
        last = None

        for current in intervals:
            if not last:
                last = current
            else:
                if current.start < last.end:
                    removed += 1
                    if last.end > current.end:
                        last = current
                else:
                    last = current

        return removed
