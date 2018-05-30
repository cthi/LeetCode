class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def computeAllPaths(cur, curPath, graph, seen, paths):
            seen.add(cur)
            curPath.append(cur)

            if cur == len(graph) - 1:
                paths.append(curPath[:])

            for nbor in graph[cur]:
                if nbor not in seen:
                    computeAllPaths(nbor, curPath, graph, seen, paths)

            curPath.pop()
            seen.remove(cur)

        paths = []
        computeAllPaths(0, [], graph, set(), paths)
        return paths
