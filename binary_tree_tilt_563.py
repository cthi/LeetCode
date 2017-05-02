# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            return abs(self.treeSum(root.left) - self.treeSum(root.right)) + \
                self.findTilt(root.left) + self.findTilt(root.right)

    def treeSum(self, root):
        if not root:
            return 0
        else:
            return root.val + \
                self.treeSum(root.left) + self.treeSum(root.right)
