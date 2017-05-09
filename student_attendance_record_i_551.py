class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        A = 0
        L = 0
        P = 0
        LC = 0

        for r in s:
            if r == 'A':
                A += 1
                LC = 0
            elif r == 'L':
                L += 1
                LC += 1

                if LC == 3:
                    return False
            else:
                P += 1
                LC = 0

            if A > 1:
                return False

        return True
