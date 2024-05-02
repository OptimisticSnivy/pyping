from collections import deque

def dfs(graph, start, visited=None):
    if visited is None: visited = set()
    visited.add(start)
    print(start, end=" ")

    for ng in graph:
        if ng not in visited:
            dfs(graph, ng, visited)


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for ng in graph[vertex]:
            if ng not in visited:
                queue.append(ng)
                visited.add(ng)

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("\nDFS Traversal:")
dfs(graph, 'A')
print("\nBFS Traversal:")
bfs(graph, 'A')
