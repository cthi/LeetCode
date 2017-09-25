class Node:
    def __init__(self):
        self.val = 0
        self.children = {}


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Node()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        root = self.trie

        for char in key:
            if char not in root.children:
                root.children[char] = Node()

            root = root.children[char]

        root.val = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        def treeSum(root):
            return root.val + sum(treeSum(v) for _, v in root.children.items())

        root = self.trie

        for char in prefix:
            if char not in root.children:
                return 0

            root = root.children[char]

        return treeSum(root)
