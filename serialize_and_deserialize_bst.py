class Codec:
    def serialize(self, root):
        serialized = []
        
        self.preorder(root, serialized)
        
        return " ".join(serialized)
        
        
    def preorder(self, root, serialized):
        if not root:
            serialized.append("None")
        else:
            serialized.append(str(root.val))
            self.preorder(root.left, serialized)
            self.preorder(root.right, serialized)


    def deserialize(self, data):
        serialized = list(reversed(data.split()))
        
        return self.buildTree(serialized)
        
    def buildTree(self, serialized):
        next = serialized.pop()
        
        if next == "None":
            return None
        else:
            node = TreeNode(int(next))
            node.left = self.buildTree(serialized)
            node.right = self.buildTree(serialized)
            
            return node

