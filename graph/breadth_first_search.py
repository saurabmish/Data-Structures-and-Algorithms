'''Breadth First Search

Traverse a graph or tree starting from a given node (root or another
arbitrary node) and exploring its neighbors, before moving down to the
next level.

A queue is used to maintain vertices.
Note that there is no 'natural' / deterministic ordering of nodes of a
graph.

Time Complexity:  O(vertices + edges)
Space Complexity: O(vertices)
The number of edges may vary between O(1) and O(n^2), depending on how
dense the graph is.
'''

from collections import deque

def bfs(graph, start):
    queue, visited = deque(), []
    queue.append(start)

    while queue:
        vertex = queue.popleft()
        if vertex in visited:
            continue
        visited.append(vertex)
        for neighbor in graph[vertex]:
            queue.append(neighbor)

    return visited
