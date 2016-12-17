class Solution(object):

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        bitfield = []

        for word in words:
            field = 0

            for char in word:
                field |= 1 << (ord(char) - ord('a'))

            bitfield.append(field)

        ans = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if (bitfield[i] & bitfield[j]) == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans
