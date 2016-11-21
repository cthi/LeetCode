class Solution(object):

    def sumNumbers(self, root):
        if not root:
            return 0

        return self.sumNumbers_h(root, "")

    def sumNumbers_h(self, root, sum):
        if not root.left and not root.right:
            return int(sum + str(root.val))

        res = 0

        if root.left:
            res += self.sumNumbers_h(root.left, sum + str(root.val))

        if root.right:
            res += self.sumNumbers_h(root.right, sum + str(root.val))

        return res
