class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder[::-1].split(',')
        return self.validate(preorder) and not preorder
        
    def validate(self, stream):
        if not stream:
            return False

        if stream.pop() == '#':
            return True
        else:
            return self.validate(stream) and self.validate(stream)
