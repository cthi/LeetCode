class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = sorted(pairs, key=lambda x: x[1])
        numPairs = 0
        lastEnd = 0

        for start, end in pairs:
            if numPairs == 0:
                numPairs += 1
                lastEnd = end
            else:
                if start > lastEnd:
                    numPairs += 1
                    lastEnd = end

        return numPairs
