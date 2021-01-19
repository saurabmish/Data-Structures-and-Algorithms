'''Depth First Search

Traverse a graph or tree starting from a given node (root or another
arbitrary node) and go as far down each branch as much as possible,
before backtracking and visiting the next branch.

A stack is used to maintain vertices.
Note that there is no 'natural' / deterministic ordering of nodes of a
graph.

Time Complexity:  O(vertices + edges)
Space Complexity: O(vertices)
The number of edges may vary between O(1) and O(n^2), depending on how
dense the graph is.
'''

def dfs(graph, start):
    stack, visited = [], []     # readable, pythonic, and faster than list()
    stack.append(start)

    while stack:
        vertex = stack.pop()
        if vertex in visited:
            continue
        visited.append(vertex)
        for neighbor in graph:
            stack.append(neighbor)

    return visited
