# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        L, ans = self.lst(root, sum)

        for i in L:
            if i == sum:
                ans += 1
        return ans

    def lst(self, root, sum):
        if not root:
            return ([], 0)
        else:
            L = [root.val]
            left, al = self.lst(root.left, sum)
            right, ar = self.lst(root.right, sum)
            ans = al + ar

            for i in left:
                L.append(root.val + i)
                if i == sum:
                    ans += 1

            for i in right:
                L.append(root.val + i)
                if i == sum:
                    ans += 1

            return (L, ans)
