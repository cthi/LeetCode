class BSTIterator(object):

    def __init__(self, root):
        if root:
            self.nodeStack = [root]
            self.appendLeft(root)
        else:
            self.nodeStack = []

    def hasNext(self):
        return len(self.nodeStack) > 0

    def next(self):
        result = self.nodeStack.pop()

        if result.right:
            self.nodeStack.append(result.right)
            self.appendLeft(result.right)

        return result.val

    def appendLeft(self, root):
        if root:
            cur = root.left

            while cur:
                self.nodeStack.append(cur)
                cur = cur.left
