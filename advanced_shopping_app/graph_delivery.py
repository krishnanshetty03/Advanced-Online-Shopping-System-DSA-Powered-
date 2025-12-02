# GRAPH IMPLEMENTATION FOR DELIVERY ROUTES + BFS PATH FINDING

from collections import deque

graph = {
    "Warehouse": ["A", "B"],
    "A": ["C", "D"],
    "B": ["D"],
    "C": ["E"],
    "D": ["E", "F"],
    "E": ["Destination"],
    "F": ["Destination"],
    "Destination": []
}

def bfs_shortest_path(start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None
