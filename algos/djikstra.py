def djikstra(graph,start):
    dists ={node: float('inf') for node in graph}
    dists[start] = 0

    visited =set()

    while len(visited) < len(graph):
        min_node = None
        min_dist = float('inf')

        for node in graph:
            if node not in visited and dists[node] < min_dist:
                min_node = node
                min_dist = dists[node]
        
        if min_node is None:
            break

        visited.add(min_node)

        for ng,wt in graph[min_node].items():
            new_dist = dists[min_node] + wt
            if new_dist < dists[ng]:
                dists[ng] = new_dist

        
    
    return dists

graph = {
    'A': {'B': 3, 'C': 4},
    'B': {'A': 3, 'C': 1, 'D': 7},
    'C': {'A': 4, 'B': 1, 'D': 2},
    'D': {'B': 7, 'C': 2}
}

start = 'A'
distances = djikstra(graph, start)
print("Shortest distances from node", start+ ":")
for node, distance in distances.items():
    print(node, "-", distance)
