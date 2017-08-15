from collections import defaultdict
from collections import Counter


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        counted = Counter([(a[0], a[1]) for a in tickets])
        used = Counter()
        dag = defaultdict(list)

        for ticket in tickets:
            dag[ticket[0]].append(ticket[1])

        for _, v in dag.items():
            v.sort()

        itinerary = []
        self.dfs(dag, "JFK", itinerary, used, counted, len(tickets), 0)

        return itinerary

    def dfs(
            self,
            dag,
            cur,
            itinerary,
            used,
            counted,
            totalTickets,
            usedTickets):
        if usedTickets == totalTickets:
            itinerary.append(cur)
            return True

        for destination in dag[cur]:
            if used[(cur, destination)] < counted[(cur, destination)]:
                used[(cur, destination)] += 1
                itinerary.append(cur)
                if self.dfs(
                        dag,
                        destination,
                        itinerary,
                        used,
                        counted,
                        totalTickets,
                        usedTickets + 1):
                    return True
                itinerary.pop()
                used[(cur, destination)] -= 1

        return False
