class Solution(object):

    def summaryRanges(self, nums):
        ranges = []
        start = None
        prev = None

        if not nums:
            return []

        for n in nums:
            if start is None:
                start = n
                prev = n
                continue

            if n - 1 == prev:
                prev = n
            else:
                if start == prev:
                    ranges.append(str(start))
                else:
                    ranges.append(str(start) + "->" + str(prev))

                start = n
                prev = n

        if start == prev:
            ranges.append(str(start))
        else:
            ranges.append(str(start) + "->" + str(prev))

        return ranges
