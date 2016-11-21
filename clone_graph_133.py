# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution:

    def cloneGraph(self, node):
        if not node:
            return None

        ht = {}
        return self.cloneGraphHelper(node, ht)

    def cloneGraphHelper(self, node, ht):
        if node in ht:
            return ht[node]
        else:
            copy = UndirectedGraphNode(node.label)
            ht[node] = copy

            for nbor in node.neighbors:
                copy.neighbors.append(self.cloneGraphHelper(nbor, ht))

            return copy
