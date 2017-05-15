# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        L = []
        self.inorderList(root, L)

        acc = 0
        gt = {}

        for n in reversed(L):
            if n not in gt:
                gt[n] = acc
                acc += n

        return self.augment(root, gt)

    def augment(self, root, gt):
        if not root:
            return None

        newRoot = TreeNode(root.val + gt[root.val])
        newRoot.left = self.augment(root.left, gt)
        newRoot.right = self.augment(root.right, gt)

        return newRoot

    def inorderList(self, root, L):
        if root:
            self.inorderList(root.left, L)
            L.append(root.val)
            self.inorderList(root.right, L)
