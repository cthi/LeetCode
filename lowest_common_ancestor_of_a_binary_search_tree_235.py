# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pList = []
        qList = []
        self.computeList(root, p, pList)
        self.computeList(root, q, qList)

        pSet = set(pList)

        for elem in reversed(qList):
            if elem in pSet:
                return elem

    def computeList(self, root, target, L):
        if root.val == target.val:
            L.append(root)
        else:
            L.append(root)

            if root.val > target.val:
                self.computeList(root.left, target, L)
            else:
                self.computeList(root.right, target, L)
