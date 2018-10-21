from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        
        self.degree = [0] * n
        self.graph = defaultdict(set)
        
        for e in edges:
            self.degree[e[0]] += 1
            self.degree[e[1]] += 1
            self.graph[e[0]].add(e[1])
            self.graph[e[1]].add(e[0])
            
        Q = [i for i in range(n) if self.degree[i] == 1]

        while Q:
            lastQ = Q[:]
            nextQ = []
            for node in Q:
                for neighbor in self.graph[node]:
                    self.degree[neighbor] -=1
                    if self.degree[neighbor] == 1:
                        nextQ.append(neighbor)
            Q = nextQ
            
        return lastQ
