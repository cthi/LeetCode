# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        hm = defaultdict(int)
        self.traverse(root, hm)

        mode_occ = max(hm.values())

        return [k for k, v in hm.items() if v == mode_occ]

    def traverse(self, root, hm):
        if root:
            hm[root.val] += 1
            self.traverse(root.left, hm)
            self.traverse(root.right, hm)
