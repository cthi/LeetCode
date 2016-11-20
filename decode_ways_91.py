class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        ht = {
            1: 'A',
            2: 'B',
            3: 'C',
            4: 'D',
            5: 'E',
            6: 'F',
            7: 'G',
            8: 'H',
            9: 'I',
            10: 'J',
            11: 'K',
            12: 'L',
            13: 'M',
            14: 'N',
            15: 'O',
            16: 'P',
            17: 'Q',
            18: 'R',
            19: 'S',
            20: 'T',
            21: 'U',
            22: 'V',
            23: 'W',
            24: 'X',
            25: 'Y',
            26: 'Z' 
        }

        return self._numDecodings(0, s, ht, {})


    def _numDecodings(self, cur, s, ht, memo):
        if cur in memo:
            return memo[cur]
        elif cur == len(s):
            return 1
        elif s[cur] == '0':
            return 0
        elif s[cur] == '1' or s[cur] == '2':
            decodings = self._numDecodings(cur + 1, s, ht, memo)
        
            if cur != len(s) - 1 and (s[cur] == '1' or (s[cur + 1] != '7' and s[cur + 1] != '8' and s[cur + 1] != '9')):
                decodings += self._numDecodings(cur + 2, s , ht, memo)
              
            memo[cur] = decodings
            
            return decodings
        else:
            return self._numDecodings(cur + 1, s, ht, memo) 
