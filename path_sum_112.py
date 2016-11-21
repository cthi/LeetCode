class Solution(object):

    def hasPathSum(self, root, sum):
        sofar = []

        if not root:
            return False

        return self.pathSum_h(root, 0, sum, sofar)

    def pathSum_h(self, root, sumSofar, sum, sofar):
        if not root.left and not root.right and sumSofar + root.val == sum:
            return True

        ans = False

        if root.left:
            sofar.append(root.val)
            ans |= self.pathSum_h(root.left, sumSofar + root.val, sum, sofar)
            sofar.pop()

        if root.right:
            sofar.append(root.val)
            ans |= self.pathSum_h(root.right, sumSofar + root.val, sum, sofar)
            sofar.pop()

        return ans
