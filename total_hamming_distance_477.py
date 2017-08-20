class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bitfield0 = [0 for i in range(32)]
        bitfield1 = [0 for i in range(32)]
        hd = 0

        for n in nums:
            for i, bit in enumerate(format(n, '032b')):
                if bit == '0':
                    bitfield0[i] += 1
                else:
                    bitfield1[i] += 1

        for a, b in list(zip(bitfield0, bitfield1)):
            hd += a * b

        return hd
