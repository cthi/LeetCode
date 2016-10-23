class Solution(object):
    def pathSum(self, root, sum):
        sofar = []
        ans = []
        
        if not root:
            return []
            
        self.pathSum_h(root, 0, sum, sofar, ans)
        
        return ans
        
    def pathSum_h(self, root, sumSofar, sum, sofar, ans):
        if not root.left and not root.right and sumSofar + root.val == sum:
            sofar.append(root.val)
            ans.append(sofar[:])
            sofar.pop()
    
        if root.left:
            sofar.append(root.val)
            self.pathSum_h(root.left, sumSofar + root.val, sum, sofar, ans)
            sofar.pop()
    
            
        if root.right:
            sofar.append(root.val)
            self.pathSum_h(root.right, sumSofar + root.val, sum, sofar, ans)
            sofar.pop()
            
