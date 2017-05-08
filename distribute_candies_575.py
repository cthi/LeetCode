class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        max_candy_pos = len(candies) // 2
        max_candy_set = len(set(candies))

        if max_candy_set > max_candy_pos:
            return max_candy_pos
        else:
            return max_candy_set
