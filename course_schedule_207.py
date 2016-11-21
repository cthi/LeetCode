ass Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for i in range(numCourses)]

        for req in prerequisites:
            graph[req[0]].append(req[1])

        seen = [False] * numCourses
        stack = [False] * numCourses

        for course in range(numCourses):
            if self.hasCycle(graph, course, seen, stack):
                return False

        return True

    def hasCycle(self, graph, course, seen, stack):
        if not seen[course]:
            seen[course] = True
            stack[course] = True

            for reqs in graph[course]:
                if stack[reqs]:
                    return True
                if self.hasCycle(graph, reqs, seen, stack):
                    return True

            stack[course] = False

        return False
