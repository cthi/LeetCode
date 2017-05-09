# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return max(
            self.pathLen(
                root.left) +
            self.pathLen(
                root.right),
            self.diameterOfBinaryTree(
                root.left),
            self.diameterOfBinaryTree(
                root.right))

    def pathLen(self, root):
        if not root:
            return 0
        return 1 + max(self.pathLen(root.left), self.pathLen(root.right))
