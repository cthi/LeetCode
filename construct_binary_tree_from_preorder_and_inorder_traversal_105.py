class Solution(object):

    def buildTree(self, preorder, inorder):
        return self.buildTreeHelper(
            preorder,
            inorder,
            0,
            len(preorder) - 1,
            0,
            len(inorder) - 1)

    def buildTreeHelper(self, preorder, inorder, p_s, p_e, i_s, i_e):
        if p_s > p_e or i_s > i_e:
            return None

        middle = preorder[p_s]
        middleIndexP = p_s
        middleIndexI = inorder.index(middle)
        len = middleIndexI - i_s

        node = TreeNode(middle)
        node.left = self.buildTreeHelper(
            preorder,
            inorder,
            middleIndexP + 1,
            middleIndexP + len,
            i_s,
            middleIndexI - 1)
        node.right = self.buildTreeHelper(
            preorder, inorder, p_s + len + 1, p_e, middleIndexI + 1, i_e)

        return node
