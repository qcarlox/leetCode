class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [0]*len(rooms)
        stack = []
        stack.append(rooms[0])
        visited[0] = 1
        while len(stack) > 0:
            roomsToVisit = stack.pop()
            for key in roomsToVisit:
                if visited[key] == 0:
                    stack.append(rooms[key])
                visited[key] = 1
        
        #print(visited)
        for room in visited:
            if room == 0:
                return False
        return True