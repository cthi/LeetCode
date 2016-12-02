class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        N = len(height)
        maxL = []
        maxR = []
        rain = 0

        for h in height:
            if not maxL:
                maxL.append(h)
            else:
                maxL.append(max(maxL[-1], h))

        for h in reversed(height):
            if not maxR:
                maxR.append(h)
            else:
                maxR.append(max(maxR[-1], h))

        maxR = list(reversed(maxR))

        for i in range(N):
            if i != 0 and i != N - 1:
                if maxL[i - 1] > height[i] and maxR[i + 1] > height[i]:
                    rain += min(maxL[i - 1], maxR[i + 1]) - height[i]

        return rain
