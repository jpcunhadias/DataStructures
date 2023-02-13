from typing import List, Tuple
import heapq

"""" 
Dijkstra's algorithm is a graph search algorithm that is used to find the shortest path from a source node to 
all other nodes in a weighted graph. The algorithm works by maintaining a priority queue of nodes, where the priority 
of each node is determined by the distance from the source node. The algorithm starts at the source node, 
adds all its neighbors to the priority queue, and sets the distance to the source node for each neighbor. It then 
repeatedly selects the node with the lowest priority (i.e., the shortest distance) from the priority queue, 
updates the distances of its neighbors, and adds them to the priority queue if they haven't been visited yet. This 
process continues until all nodes have been visited.

The algorithm can be implemented using a min-priority queue to efficiently select the node with the lowest priority, 
or using a simple list and sorting it after each update.

Time complexity: O(E log V) where E is the number of edges and V is the number of vertices.
"""


class Graph:
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, src: int, dest: int, weight: int):
        self.adj_list[src].append((dest, weight))
        self.adj_list[dest].append((src, weight))


def dijkstra(graph: Graph,
             start: int,
             end: int) -> Tuple[int, List[int]]:

    visited = [False] * graph.num_vertices
    distances = [float("inf")] * graph.num_vertices
    distances[start] = 0
    queue = [(0, start, [start])]
    while queue:
        distance, node, path = heapq.heappop(queue)
        if node == end:
            return distance, path
        if not visited[node]:
            visited[node] = True
            for neighbor, weight in graph.adj_list[node]:
                if not visited[neighbor]:
                    new_distance = distance + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        heapq.heappush(queue, (new_distance, neighbor, path + [neighbor]))
    return -1, []
