class Solution(object):

    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        r1 = (C - A) * (D - B)
        r2 = (G - E) * (H - F)

        left = max(A, E)
        right = min(C, G)
        top = min(D, H)
        bot = max(B, F)

        if left < right and bot < top:
            return r1 + r2 - (right - left) * (top - bot)
        else:
            return r1 + r2
