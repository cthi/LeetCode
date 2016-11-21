# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self._sortedArrayToBST(nums, 0, len(nums) - 1)

    def _sortedArrayToBST(self, nums, start, end):
        if start > end:
            return None

        middle = (start + end) // 2

        node = TreeNode(nums[middle])
        node.left = self._sortedArrayToBST(nums, start, middle - 1)
        node.right = self._sortedArrayToBST(nums, middle + 1, end)

        return node
