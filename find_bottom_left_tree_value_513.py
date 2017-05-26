# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.findBottomLeftValue_h(root, 0)[0]

    def findBottomLeftValue_h(self, root, level):
        if not root:
            return (None, float("-inf"))
        elif not root.left and not root.right:
            return (root.val, level)
        else:
            left = self.findBottomLeftValue_h(root.left, level + 1)
            right = self.findBottomLeftValue_h(root.right, level + 1)

            if left[1] >= right[1]:
                return left
            else:
                return right
