# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        elif not s:
            return False

        return self.sameTree(
            s,
            t) or self.isSubtree(
            s.left,
            t) or self.isSubtree(
            s.right,
            t)

    def sameTree(self, s, t):
        if not s and not t:
            return True
        elif (not s and t) or (s and not t):
            return False

        return s.val == t.val and self.sameTree(
            s.left, t.left) and self.sameTree(
            s.right, t.right)
