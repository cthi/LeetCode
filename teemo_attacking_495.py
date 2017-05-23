class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        last = float('-inf')
        poisoned = 0

        for t in timeSeries:
            if last + duration > t:
                poisoned += t - last
            else:
                poisoned += duration

            last = t

        return poisoned
