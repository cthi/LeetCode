class Solution(object):

    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses = sorted(houses)
        heaters = sorted(heaters)
        j = 0
        maxRad = float('-inf')

        for house in houses:
            minRadFromHouse = abs(heaters[j] - house)

            while heaters[j] <= house:
                minRadFromHouse = min(minRadFromHouse, abs(heaters[j] - house))
                if j < len(heaters) - 1:
                    j += 1
                else:
                    break

            minRadFromHouse = min(minRadFromHouse, abs(heaters[j] - house))
            if j > 0:
                j -= 1

            maxRad = max(maxRad, minRadFromHouse)

        return maxRad
