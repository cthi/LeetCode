# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ht = {}
        
        return self.robHelper(root, ht)
        
        
    def robHelper(self, root, ht):
        if not root:
            return 0
            
        if root in ht:
            return ht[root]
        
        a = self.robHelper(root.left, ht) + self.robHelper(root.right, ht)
        b = root.val
        if root.left:
            b += self.robHelper(root.left.left, ht) + self.robHelper(root.left.right, ht)
        if root.right:
            b += self.robHelper(root.right.left, ht) + self.robHelper(root.right.right, ht)
            
        ans = max(a,b)
        ht[root] = ans
        
        return ans
