from dataclasses import dataclass


@dataclass
class Edge:
    end: str
    weight: float = None
    def __hash__(self):
        return hash(self.end)


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, start_vertex, end_vertex, weight=None):
        edge = Edge(end=end_vertex, weight=weight)
        if (not start_vertex in self.nodes.keys()) or (not edge in self.nodes[start_vertex]):
            if not start_vertex in self.nodes.keys():
                self.nodes[start_vertex] = []
            if not end_vertex in self.nodes.keys():
                self.nodes[end_vertex] = []
            self.nodes[start_vertex].append(edge)
