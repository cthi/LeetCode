# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        sums = defaultdict(int)
        self.findFrequentTreeSum_h(root, sums)
        mostFreq = max(sums.values())

        return [x[0] for x in sums.items() if x[1] == mostFreq]

    def findFrequentTreeSum_h(self, root, sums):
        if not root:
            return 0

        sts = root.val + \
            self.findFrequentTreeSum_h(root.left, sums) + self.findFrequentTreeSum_h(root.right, sums)
        sums[sts] += 1

        return sts
