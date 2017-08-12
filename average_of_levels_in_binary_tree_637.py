class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        avg = []
        Q = [root]

        while Q:
            tmp = []
            nums = 0

            for node in Q:
                nums += node.val

                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)

            avg.append(nums / len(Q))
            Q = tmp

        return avg
