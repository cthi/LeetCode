class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        slices = 0
        seqDiff = 0
        seqLen = 0

        for i in range(len(A)):
            if i == 0:
                seqLen = 1
            elif seqLen == 1:
                seqDiff = A[i] - A[i - 1]
                seqLen = 2
            elif A[i] - A[i - 1] == seqDiff:
                seqLen += 1
            else:
                slices += ((seqLen - 2) * (seqLen - 1)) // 2
                seqLen = 2
                seqDiff = A[i] - A[i - 1]

        if seqLen > 2:
            slices += ((seqLen - 2) * (seqLen - 1)) // 2

        return slices
