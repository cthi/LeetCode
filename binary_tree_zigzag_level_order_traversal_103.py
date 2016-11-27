# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        Q = [root]
        ans = []
        count = 0

        while Q:
            ans.append([x.val for x in Q])
            next = []
            count += 1
            for node in reversed(Q):
                if count % 2 == 0:
                    if node.left:
                        next.append(node.left)
                    if node.right:
                        next.append(node.right)
                else:
                    if node.right:
                        next.append(node.right)
                    if node.left:
                        next.append(node.left)

            Q = next

        return ans
