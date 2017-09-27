class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def checkValidString_h(s, idx, nopen, memo):
            if idx == len(s):
                return nopen == 0
            elif (idx, nopen) in memo:
                return memo[(idx, nopen)]
            elif s[idx] == '(':
                memo[(idx, nopen)] = checkValidString_h(
                    s, idx + 1, nopen + 1, memo)
            elif s[idx] == ')':
                if nopen <= 0:
                    memo[(idx, nopen)] = False
                else:
                    memo[(idx, nopen)] = checkValidString_h(
                        s, idx + 1, nopen - 1, memo)
            else:
                if checkValidString_h(s, idx + 1, nopen, memo):
                    memo[(idx, nopen)] = True
                else:
                    memo[(idx, nopen)] = checkValidString_h(
                        s, idx + 1, nopen + 1, memo) or checkValidString_h(s, idx + 1, nopen - 1, memo)

            return memo[(idx, nopen)]
        return checkValidString_h(s, 0, 0, {})
