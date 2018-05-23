# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def bstMax(root):
            if not root:
                return float('-inf')

            return max(root.val, bstMax(root.right))

        def bstMin(root):
            if not root:
                return float('inf')

            return min(root.val, bstMin(root.left))

        if not root:
            return float('inf')

        l_max = bstMax(root.left)
        r_min = bstMin(root.right)

        m = min(
            self.minDiffInBST(root.right),
            self.minDiffInBST(root.left),
        )

        if l_max != float('-inf'):
            m = min(m, root.val - l_max)

        if r_min != float('inf'):
            m = min(m, r_min - root.val)

        return m
