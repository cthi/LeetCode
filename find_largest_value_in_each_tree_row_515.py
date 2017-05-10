# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []

        output = []
        Q = [root]
        C = []

        while Q:
            best = float('-inf')

            for node in Q:
                best = max(best, node.val)

                if node.left:
                    C.append(node.left)
                if node.right:
                    C.append(node.right)

            Q = C
            C = []
            output.append(best)

        return output
