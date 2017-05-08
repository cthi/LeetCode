class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        a = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        b = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        c = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}

        output = []

        for w in words:
            z = w.lower()
            if self.canBeTyped(
                a,
                z) or self.canBeTyped(
                b,
                z) or self.canBeTyped(
                c,
                    z):
                output.append(w)

        return output

    def canBeTyped(self, alpha, w):
        for chr in w:
            if chr not in alpha:
                return False

        return True
