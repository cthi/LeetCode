class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        lcsLen = self.lcs(word1, word2, len(word1) - 1, len(word2) - 1, {})

        return len(word1) - lcsLen + len(word2) - lcsLen

    def lcs(self, word1, word2, i, j, memo):
        if i == -1 or j == -1:
            return 0
        elif (i, j) in memo:
            return memo[(i, j)]
        elif word1[i] != word2[j]:
            memo[(i, j)] = max(self.lcs(word1, word2, i, j - 1, memo),
                               self.lcs(word1, word2, i - 1, j, memo))
            return memo[(i, j)]
        else:
            memo[(i, j)] = 1 + self.lcs(word1, word2, i - 1, j - 1, memo)
            return memo[(i, j)]
