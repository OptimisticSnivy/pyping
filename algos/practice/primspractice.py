def prim(graph, start_node):
    mst = []
    visited = set()
    visited.add(start_node)

    while len(visited) < len(graph):
        min_cost = float('inf')
        min_edge = None
        
        for src in visited:
            for dest, cost in graph[src]:
                if dest not in visited and cost < min_cost:
                    min_cost = cost
                    min_edge = (src, dest, cost)

        if min_edge:
            mst.append(min_edge)
            visited.add(min_edge[1])
    return mst


# the tuple is of format source,destination,edge
# Example usage
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 4), ('D', 5)],
    'C': [('A', 3), ('B', 4), ('D', 6)],
    'D': [('B', 5), ('C', 6)]
}

start_node = 'A'  # Specify the starting node
minimum_spanning_tree = prim(graph, start_node)
print("Minimum Spanning Tree:", minimum_spanning_tree)
