class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def is_self_dividing(n):
            orig = n
            
            while orig > 0:
                if (orig % 10) == 0 or n % (orig % 10) != 0:
                    return False
                orig -= orig % 10
                orig /= 10
            
            return True
                
            
        return [i for i in range(left, right + 1) if is_self_dividing(i)]
