def kruskals(graph):
    mst = []
    edges = []

    for node in graph:
        for ng,wt in graph[node]:
            edges.append((wt, node,ng))
    
    edges.sort()

    disj = {node: node for node in graph}
    
    def find(node):
        if disj[node] != node:
            disj[node] = find(disj[node])
        return disj[node]

    def union(u,v):
        disj[find(u)] = find(v)
    
    for wt,u,v in edges:
        if find(u) != find(v):
            mst.append((u,v,wt))
            union(u,v)

    return mst
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 4), ('D', 5)],
    'C': [('A', 3), ('B', 4), ('D', 6)],
    'D': [('B', 5), ('C', 6)]
}

minimum_spanning_tree = kruskals(graph)
print("Minimum Spanning Tree:", minimum_spanning_tree)
