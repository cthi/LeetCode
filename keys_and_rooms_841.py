class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        def visitRooms(curRoom, rooms, visited):
            if curRoom in visited:
                return

            visited.add(curRoom)

            for nextRoom in rooms[curRoom]:
                visitRooms(nextRoom, rooms, visited)

        visited = set()
        visitRooms(0, rooms, visited)

        return len(visited) == len(rooms)
