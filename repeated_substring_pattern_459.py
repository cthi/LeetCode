class Solution(object):

    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        res = ""

        for i in range(len(str) // 2):
            res += str[i]

            if (len(str) - (i + 1)) % len(res) != 0:
                continue

            ci = 0
            for j in range(i + 1, len(str)):
                if res[ci] != str[j]:
                    break
                else:
                    if j == len(str) - 1 and ci == len(res) - 1:
                        return True

                    ci += 1
                    j += 1

                    if ci == len(res):
                        ci = 0

        return False
