class WordDictionary(object):

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word):
        self.trie.add(word)

    def search(self, word):
        return self.trie.search(word, 0, self.trie.root)


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

    def search(self, word, index, node):
        if index == len(word):
            return node.isWord

        w = word[index]

        if w != '.':
            if not node.children[ord(w) - ord('a')]:
                return False

            return self.search(
                word,
                index + 1,
                node.children[
                    ord(w) - ord('a')])
        else:
            ans = False

            for child in node.children:
                if child:
                    ans = ans or self.search(word, index + 1, child)

            return ans
