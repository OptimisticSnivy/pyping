import heapq

def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1]) 

def a_star(graph, start, goal):
    visited = set()
    openl = [(0,start)]
    heapq.heapify(openl)

    while openl:
        curr_cost, curr_node = heapq.heappop(openl)

        if curr_node == goal:
            return True
        
        visited.add(curr_node)

        for ng, wt in graph[curr_node]:
            if ng not in visited:
                new_cost = curr_cost + wt
                total_cost = new_cost + heuristic(ng, goal)
                heapq.heappush(openl, (total_cost,ng))


    return False
# Example graph represented as an adjacency list with weighted edges
graph = {
    (0, 0): [((0, 1), 1), ((1, 0), 1)],
    (0, 1): [((0, 0), 1), ((1, 1), 1)],
    (1, 0): [((0, 0), 1), ((1, 1), 1)],
    (1, 1): [((0, 1), 1), ((1, 0), 1)]
}

start_node = (0, 0)
goal_node = (1, 1)

found = a_star(graph, start_node, goal_node)
if found:
    print("Goal is reachable from the start node.")
else:
    print("Goal is not reachable from the start node.")
