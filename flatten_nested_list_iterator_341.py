class NestedIterator(object):
    def __init__(self, nestedList):
        self.stack = list(reversed(nestedList))
        

    def next(self):
        return self.stack.pop().getInteger()
        
    
    def move(self):
        while self.stack and not self.stack[-1].isInteger():
            for e in reversed(self.stack.pop().getList()):
                self.stack.append(e)
                
                
    def hasNext(self):
        self.move()
        return len(self.stack) > 0
        
