class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word:
            return True

        return self.allCaps(word) or self.noCaps(word) or self.oneCap(word)

    def allCaps(self, word):
        for chr in word:
            if ord(chr) > ord('Z') or ord(chr) < ord('A'):
                return False

        return True

    def noCaps(self, word):
        for chr in word:
            if ord(chr) > ord('z') or ord(chr) < ord('a'):
                return False

        return True

    def oneCap(self, word):
        return self.allCaps(word[0]) and self.noCaps(word[1:])
