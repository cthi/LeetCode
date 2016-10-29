class Solution(object):
    def longestConsecutive(self, nums):
        uf = UnionFind(len(nums))
        ht = {}
        
        cur = 0
        
        for num in nums:
            ht[num] = cur
            cur += 1
            
        for num in nums:
            if num - 1 in ht:
                uf.union(ht[num - 1], ht[num])
            if num + 1 in ht:
                uf.union(ht[num + 1], ht[num])
        
        return(max(uf.size))
        
        
class UnionFind:
    def __init__(self, n):
        self.ids = list(range(n))
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
        
        if i == j:
            return
        
        if self.size[i] > self.size[j]:
            self.ids[j] = i
            self.size[i] += self.size[j]
        else:
            self.ids[i] = j
            self.size[j] += self.size[i]

