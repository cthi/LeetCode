# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        L = []
        self.inorder(root, L)

        lowest = float("inf")
        print(L)
        for i in range(1, len(L)):
            lowest = min(lowest, abs(L[i] - L[i - 1]))

        return lowest

    def inorder(self, root, L):
        if root:
            self.inorder(root.left, L)
            L.append(root.val)
            self.inorder(root.right, L)
