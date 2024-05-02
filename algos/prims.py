def prim(graph, start_node):
    # Initialize variables
    mst = []  # Minimum Spanning Tree
    visited = set()  # Set to keep track of visited nodes
    visited.add(start_node)
    
    # Main loop
    while len(visited) < len(graph):
        min_cost = float('inf')
        min_edge = None
        
        # Find the minimum edge that connects a visited node to an unvisited node
        for src in visited:
            for dest, cost in graph[src]:
                if dest not in visited and cost < min_cost:
                    min_cost = cost
                    min_edge = (src, dest, cost)
        
        # Add the minimum edge to the MST and mark the destination node as visited
        if min_edge:
            mst.append(min_edge)
            visited.add(min_edge[1])
    
    return mst

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
