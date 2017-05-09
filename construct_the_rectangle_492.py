class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        L = int(math.sqrt(area))

        while True:
            W = area // L

            if W * L == area:
                return [W, L]

            L -= 1
