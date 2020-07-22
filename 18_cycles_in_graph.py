# Given an undirected graph, determine if a cycle exists in the graph.

# Here is a function signature:


def find_cycle(graph):
    def traverse(graph, visited_vertexes):
        for vertex in graph.keys():
            if vertex in visited_vertexes:
                return True
            visited_vertexes.add(vertex)
            if traverse(graph[vertex], visited_vertexes):
                return True
        return False
    visited_vertexes = set()
    return traverse(graph, visited_vertexes)


graph = {
  'a': {'a2': {}, 'a3': {}},
  'b': {'b2': {}},
  'c': {}
}
print(find_cycle(graph))
# False
graph['c'] = graph
print(find_cycle(graph))
# True