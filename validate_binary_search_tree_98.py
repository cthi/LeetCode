# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSTHelper(root, float('-inf'), float('inf'))


    def isValidBSTHelper(self, root, low, hi):
        if not root:
            return True
        elif root.val <= low or root.val >= hi:
            return False
        else:
            return self.isValidBSTHelper(root.left, low, root.val) and self.isValidBSTHelper(root.right, root.val, hi)
