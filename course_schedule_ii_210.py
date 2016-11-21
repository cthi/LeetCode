class Solution(object):

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for i in range(numCourses)]

        for req in prerequisites:
            graph[req[0]].append(req[1])

        seen = [False] * numCourses
        stack = [False] * numCourses
        order = []

        for course in range(numCourses):
            if not self.topsort(graph, course, seen, order, stack):
                return []

        return order

    def topsort(self, graph, course, seen, order, stack):
        if not seen[course]:
            seen[course] = True
            stack[course] = True

            for req in graph[course]:
                if stack[req]:
                    return False
                if not self.topsort(graph, req, seen, order, stack):
                    return False

            stack[course] = False
            order.append(course)

        return True
