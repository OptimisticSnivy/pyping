def kruskals(graph):
    # Initialize variables
    mst = []  # Minimum Spanning Tree
    edges = []

    # Create a list of all edges in the graph
    for node in graph:
        for neighbor, weight in graph[node]:
            edges.append((weight, node, neighbor))

    # Sort the edges by weight
    edges.sort()
    print(edges)

    # Create a dictionary to keep track of which node belongs to which set
    disjoint_sets = {node: node for node in graph}

    # Define functions to find and union sets
    def find(node):
        if disjoint_sets[node] != node:
            disjoint_sets[node] = find(disjoint_sets[node])
        return disjoint_sets[node]

    def union(u, v):
        disjoint_sets[find(u)] = find(v)

    # Iterate through sorted edges and add to MST if they don't form a cycle
    for weight, u, v in edges:
        if find(u) != find(v):
            mst.append((u, v, weight))
            union(u, v)

    return mst

# Example usage
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 4), ('D', 5)],
    'C': [('A', 3), ('B', 4), ('D', 6)],
    'D': [('B', 5), ('C', 6)]
}

minimum_spanning_tree = kruskals(graph)
print("Minimum Spanning Tree:", minimum_spanning_tree)
