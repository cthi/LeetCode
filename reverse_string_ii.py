class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        counter = 0
        index = 0
        rev = True
        buf = []
        output = ""

        while index < len(s):
            if rev:
                buf.append(s[index])
            else:
                output += (s[index])

            counter += 1
            index += 1

            if counter == k:
                rev = not rev
                counter = 0
                output += ("".join(reversed(buf)))
                buf = []

        if buf:
            output += ("".join(reversed(buf)))

        return output
