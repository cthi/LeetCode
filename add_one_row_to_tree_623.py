class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            newRoot = TreeNode(v)
            newRoot.left = root
            return newRoot
        else:
            self.addOneRow_h(root, v, d)
            return root

    def addOneRow_h(self, root, v, d):
        if not root:
            return
        if d == 2:
            newLeft = TreeNode(v)
            newRight = TreeNode(v)
            newLeft.left = root.left
            newRight.right = root.right
            root.left = newLeft
            root.right = newRight
        else:
            self.addOneRow_h(root.left, v, d - 1)
            self.addOneRow_h(root.right, v, d - 1)
