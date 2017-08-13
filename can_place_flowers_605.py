class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        planted = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (
                    i == 0 or flowerbed[i - 1] != 1) and (i == len(flowerbed) - 1 or flowerbed[i + 1] != 1):
                flowerbed[i] = 1
                planted += 1

        return planted >= n
