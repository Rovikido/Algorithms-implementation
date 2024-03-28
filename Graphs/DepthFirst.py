from template import Edge, Graph


# Complexity is O(V+E) since we avoid visiting procesed vertecies


class DepthFirstSearch(Graph):
    def __DFS_process_node(self, node, search_value, visited):
        print(f"({node})", end=" -> ")
        if node == search_value:
                print(f'Found value {node}')
                return
        
        visited.append(node)

        for edge in self.nodes[node]:
            if not edge.end in visited:
                self.__DFS_process_node(edge.end, search_value, visited)


    def DFS(self, start_node, search_value):
        if not start_node in self.nodes.keys():
            return None
        
        visited = []
        self.__DFS_process_node(start_node, search_value, visited)
    

graph = DepthFirstSearch()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

graph.DFS(0, 3)
