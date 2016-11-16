# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        res = self.findNode(root, None, key)
        
        if not res:
            return root
        else:
            toRemove = res[0]
            parent = res[1]
            
        if not toRemove.left and not toRemove.right:
            if parent:
                self.nodeReplace(parent, toRemove, None)
            else:
                root = None
        elif not toRemove.left and toRemove.right:
            if parent:
                self.nodeReplace(parent, toRemove, toRemove.right)
            else:
                root = toRemove.right
        elif not toRemove.right and toRemove.left:
            if parent:
                self.nodeReplace(parent, toRemove, toRemove.left)
            else:
                root = toRemove.left
        else:
            replacement = toRemove.left
            ref = replacement
            
            while ref.right:
                ref = ref.right
                
            ref.right = toRemove.right
            
            if parent:
                self.nodeReplace(parent, toRemove, replacement)
            else:
                root = replacement
                
        return root
        
        
    def nodeReplace(self, parent, toReplace, replacement):
        if parent.left == toReplace:
            parent.left = replacement
        else:
            parent.right = replacement


    def findNode(self, root, parent, key):
        if not root:
            return None
        elif root.val == key:
            return (root, parent)
        else:
            res = self.findNode(root.left, root, key)
                
            if res:
                return res
            
            res = self.findNode(root.right, root, key)
            
            if res:
                return res
