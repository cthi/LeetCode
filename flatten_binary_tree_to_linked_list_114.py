class Solution(object):
    def flatten(self, root):
        self.to_ll(root)

        
    def to_ll(self, root):
        if not root:
            return None
    
        rootRef = root
        rightRef = root.right
        
        root.right = self.to_ll(root.left)
        root.left = None
        
        while root.right:
            root = root.right

        root.right = self.to_ll(rightRef)

        return rootRef
