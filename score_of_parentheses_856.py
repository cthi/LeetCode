class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        def score(S):
            S.pop()
            ret = 0

            while S[-1] == '(':
                ret += 2 * score(S)

            S.pop()

            return 1 if ret == 0 else ret

        S = list(reversed(S))
        ret = 0

        while S:
            ret += score(S)

        return ret
