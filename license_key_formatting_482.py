class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        output = []
        count = 0

        charCount = 0

        for c in S:
            if c != '-':
                charCount += 1

        for c in reversed(S):
            if c == '-':
                continue
            elif ord(c) >= ord('a') and ord(c) <= ord('z'):
                output += chr(ord(c) - (ord('a') - ord('A')))
            else:
                output += c

            charCount -= 1
            count += 1

            if count == K and charCount > 0:
                output += '-'
                count = 0

        return "".join(reversed(output))
