class Solution(object):

    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        minElem = float('inf')
        minElem2 = float('inf')

        for n in nums:
            if n <= minElem:
                minElem = n
            elif n <= minElem2:
                minElem2 = n
            else:
                return True

        return False
