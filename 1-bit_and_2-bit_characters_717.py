class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        
        def isOneBitCharacter_h(bits, pos, good):
            if pos == len(bits):
                return good

            res = False
            if bits[pos] == 0:
                res = res or isOneBitCharacter_h(bits, pos + 1, True)
            if bits[pos] == 1 and pos != len(bits) - 1:
                res = res or isOneBitCharacter_h(bits, pos + 2, False)

            return res

        return isOneBitCharacter_h(bits, 0, False)
