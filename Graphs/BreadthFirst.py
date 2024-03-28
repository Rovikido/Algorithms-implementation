from template import Edge, Graph


# Complexity is O(V+E) since we avoid visiting procesed vertecies


class BreadthFirstGraph(Graph):
    def BFS(self, start_node, search_value):
        if not start_node in self.nodes.keys():
            return None
        
        queue = [start_node]
        visited = []

        while queue:
            print(f"({queue[0]})", end=" -> ")
            visited.append(queue[0])
            if queue[0] == search_value:
                print(f'Found value {queue[0]}')
                return
            for edge in self.nodes[queue[0]]:
                if isinstance(edge, Edge) and not edge.end in visited:
                    queue.append(edge.end)

            del queue[0]
    

graph = BreadthFirstGraph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 4)

graph.BFS(0, 4)
