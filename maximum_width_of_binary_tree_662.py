from collections import defaultdict


class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def walkTree(root, level, offset, dict):
            if not root:
                return

            dict[level].append(offset)

            if level == 0:
                left = offset - 1
                right = offset + 1
            else:
                offsetPos = abs(offset)
                left = 2 * offsetPos
                right = 2 * offsetPos - 1

                if offset < 0:
                    left *= -1
                    right *= -1
                if offset > 0:
                    left, right = right, left

            walkTree(root.left, level + 1, left, dict)
            walkTree(root.right, level + 1, right, dict)

        if root and not root.left and not root.right:
            return 1

        dict = defaultdict(list)
        walkTree(root, 0, 0, dict)
        maxWidth = 0

        for _, vals in dict.items():
            a, b = min(vals), max(vals)
            maxMaybe = abs(a - b)

            if a * b > 0:
                maxMaybe += 1

            maxWidth = max(maxWidth, maxMaybe)

        return maxWidth
