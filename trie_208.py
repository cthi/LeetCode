class TrieNode(object):

    def __init__(self):
        self.children = [None] * 26
        self.isWord = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            index = ord(char) - ord('a')

            if not node.children[index]:
                node.children[index] = TrieNode()

            node = node.children[index]

        node.isWord = True

    def search(self, word):
        node = self.root

        for char in word:
            index = ord(char) - ord('a')

            if not node.children[index]:
                return False

            node = node.children[index]

        return node.isWord

    def startsWith(self, prefix):
        node = self.root

        for char in prefix:
            index = ord(char) - ord('a')

            if not node.children[index]:
                return False

            node = node.children[index]

        return True
