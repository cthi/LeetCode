class Node:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        node = self.root

        for w in word:
            if not node.children[ord(w) - ord('a')]:
                node.children[ord(w) - ord('a')] = Node()

            node = node.children[ord(w) - ord('a')]

        node.isWord = True

    def findShortestPrefix(self, word):
        node = self.root
        prefix = ""

        for w in word:
            if node.children[ord(w) - ord('a')]:
                prefix += w
                node = node.children[ord(w) - ord('a')]
            else:
                return None

            if node.isWord:
                return prefix


class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        t = Trie()

        for word in dict:
            t.add(word)

        newSentence = []

        for word in sentence.split():
            prefix = t.findShortestPrefix(word)

            if not prefix:
                newSentence.append(word)
            else:
                newSentence.append(prefix)

        return " ".join(newSentence)
