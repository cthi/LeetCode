# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """

        def findRoot(root, L, R):
            if not root:
                return None

            if L <= root.val <= R:
                return root
            elif root.val < L:
                return findRoot(root.right, L, R)
            else:
                return findRoot(root.left, L, R)

        def trimBST_h(root, L, R):
            if root:
                if root.left and root.left.val < L:
                    root.left = findRoot(root.left, L, R)
                if root.right and root.right.val > R:
                    root.right = findRoot(root.right, L, R)

                trimBST_h(root.left, L, R)
                trimBST_h(root.right, L, R)

        newRoot = findRoot(root, L, R)
        trimBST_h(newRoot, L, R)
        return newRoot
