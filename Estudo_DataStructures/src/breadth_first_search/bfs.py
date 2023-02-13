from typing import List, Tuple


class Graph:
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, src: int, dest: int):
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)


def breadth_first_search(graph: Graph,
                         start: int,
                         end: int) -> Tuple[bool, List[int]]:
    visited = [False] * graph.num_vertices
    queue = [(start, [start])]
    while queue:
        node, path = queue.pop(0)
        if node == end:
            return True, path
        for neighbor in graph.adj_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, path + [neighbor]))
    return False, []
