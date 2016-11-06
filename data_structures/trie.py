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

  
  def search(self, word):
    node = self.root
    
    for w in word:
      if not node.children[ord(w) - ord('a')]:
        return False

      node = node.children[ord(w) - ord('a')]

    return node.isWord

