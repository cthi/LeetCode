class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        bestIndex = self.maxInd(nums)
        node = TreeNode(nums[bestIndex])
        node.left = self.constructMaximumBinaryTree(nums[0:bestIndex])
        node.right = self.constructMaximumBinaryTree(
            nums[bestIndex + 1:len(nums)])

        return node

    def maxInd(self, nums):
        best = float('-inf')
        bestIndex = 0

        for i, x in enumerate(nums):
            if x > best:
                best = x
                bestIndex = i

        return bestIndex
