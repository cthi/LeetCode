from collections import defaultdict
import bisect


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        dict = defaultdict(list)

        for i, chr in enumerate(s):
            dict[chr].append(i)

        bestWord = ""

        for word in d:
            if self.isSubseq(word, dict):
                if len(word) > len(bestWord):
                    bestWord = word
                elif len(word) == len(bestWord) and word < bestWord:
                    bestWord = word

        return bestWord

    def isSubseq(self, word, dict):
        last = -1

        for w in word:
            oldLast = last

            for pos in dict[w]:
                if pos > last:
                    last = pos
                    break

            if oldLast == last:
                return False

        return True
