class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [
            [
                x ^ 1 for x in reversed(row)
            ] for row in A
        ]
