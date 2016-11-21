class Solution(object):

    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)

        res = []

        for interval in intervals:
            if not res:
                res.append(interval)
            else:
                last = res[-1]
                if last.end >= interval.start:
                    if interval.end > last.end:
                        last.end = interval.end
                else:
                    res.append(interval)

        return res
