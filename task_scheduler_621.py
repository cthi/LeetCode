from collections import Counter


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        def findNextBestTask(time, remainingTasks, lastSeen, n):
            bestTaskId = -1
            bestTaskCount = 0

            for taskId, lastSeen in lastSeen.items():
                if lastSeen + \
                        n < time and remainingTasks[taskId] > bestTaskCount:
                    bestTaskId = taskId
                    bestTaskCount = remainingTasks[taskId]

            return bestTaskId

        time = 0
        completed = 0
        remainingTasks = Counter(tasks)
        lastSeen = {id: float('-inf') for id in remainingTasks.keys()}

        while completed < len(tasks):
            taskId = findNextBestTask(time, remainingTasks, lastSeen, n)

            if taskId != -1:
                completed += 1
                remainingTasks[taskId] -= 1
                lastSeen[taskId] = time

            time += 1

        return time
