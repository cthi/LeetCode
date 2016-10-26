class Solution(object):
    def buildTree(self, inorder, postorder):
        return self.buildTreeHelper(inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1)
        
    def buildTreeHelper(self, inorder, postorder, i_s, i_e, p_s, p_e):
        if i_s > i_e or p_s > p_e:
            return None
            
        middle = postorder[p_e]
        middleIndexI = inorder.index(middle)
        middleIndexE = p_s + (middleIndexI - i_s)
        
        node = TreeNode(middle)
        node.left = self.buildTreeHelper(inorder, postorder, i_s, middleIndexI - 1, p_s, middleIndexE - 1)
        node.right = self.buildTreeHelper(inorder, postorder, middleIndexI + 1, i_e, middleIndexE, p_e - 1)
        
        return node
