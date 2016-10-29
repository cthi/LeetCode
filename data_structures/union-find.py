class UnionFind:
    def __init__(self, size):
        self.ids = list(range(size))
        self.size = [1] * n


    def root(self, key):
        while key != self.ids[key]:
          self.ids[key] = self.ids[self.ids[key]]
          key = self.ids[key]
        return key


    def find(self, p, q):
        return self.root(p) == self.root(q)


    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        
        if self.size[i] > self.size[j]:
            self.ids[j] = i
            self.size[i] += self.size[j]
        else:
            self.ids[i] = j
            self.size[j] += self.size[i]
 
