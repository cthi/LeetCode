class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        old_run = 0
        run = 1
        count = 0

        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                run += 1;
                if old_run:
                    old_run -= 1
                    count += 1
            else:
                old_run = run - 1
                run = 1
                count += 1

        return count
