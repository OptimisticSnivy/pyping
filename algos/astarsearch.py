import heapq

def heuristic(node, goal):
    """
    A simple heuristic function to estimate the cost from node to goal.
    This function can be customized based on the problem domain.
    """
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def a_star(graph, start, goal):
    visited = set()
    open_list = [(0, start)]
    heapq.heapify(open_list)
    
    while open_list:
        current_cost, current_node = heapq.heappop(open_list)
        
        if current_node == goal:
            return True
        
        visited.add(current_node)
        
        for neighbor, weight in graph[current_node]:
            if neighbor not in visited:
                new_cost = current_cost + weight
                total_cost = new_cost + heuristic(neighbor, goal)
                heapq.heappush(open_list, (total_cost, neighbor))
        
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


# Import Required Modules:
#     We import the heapq module, which provides heap queue operations. This module is used to implement the priority queue for efficient retrieval of the node with the lowest total cost.
#
# Heuristic Function (heuristic):
#     This function calculates a heuristic value for a given node, estimating the cost to reach the goal from that node. In this implementation, it calculates the Manhattan distance between the current node and the goal node.
#
# A Search Algorithm* (a_star):
#     It takes three parameters: graph, start, and goal.
#     visited is a set to keep track of visited nodes.
#     open_list is a priority queue initialized with the start node and its cost. We use heapq.heapify() to transform the list into a heap, maintaining the lowest-cost node at the top.
#     The function runs a loop while there are elements in the open_list.
#     Within each iteration:
#         It extracts the node with the lowest total cost from the open_list using heapq.heappop().
#         If the current node is the goal node, it returns True, indicating the goal is reachable.
#         Otherwise, it adds the current node to the visited set.
#         It then iterates through the neighbors of the current node:
#             For each neighbor:
#                 If the neighbor hasn't been visited:
#                     It calculates the cost to reach the neighbor (including the cost to reach the current node and the weight of the edge).
#                     It calculates the total cost for the neighbor, which is the sum of the new cost and the heuristic cost from the neighbor to the goal.
#                     It pushes the neighbor and its total cost to the open_list using heapq.heappush().
#     If the loop finishes without finding the goal node, it returns False, indicating the goal is not reachable.
#
# Example Graph:
#     The graph is represented as an adjacency list with weighted edges, similar to the previous example.
#
# Start and Goal Nodes:
#     start_node and goal_node are defined similarly to the previous example.
#
# Search Execution:
#     It calls the a_star function with the provided graph, start node, and goal node.
#     If the goal is reachable, it prints "Goal is reachable from the start node." Otherwise, it prints "Goal is not reachable from the start node."
