class Graph:
    def __init__(self):
        self.graph = {}
        self._bfsPath = []

    def addEdge(self, node1, node2):
        """Create a path from node1 to node2"""
        if node1 in self.graph:
            self.graph[node1] += [node2]
        else:
            self.graph[node1] = [node2]

        if node2 not in self.graph:
            self.graph[node2] = []

    def dfs(self, start, end):
        """perform a depth first search from specified start node to end node"""
        if start == end:
            return True

        if not (start in self.graph or end in self.graph):
            return False

        rv = False
        for node in self.graph[start]:
            rv = rv or self.dfs(node, end)
            if rv:
                return rv

        return rv

    # implement dfs that doesn't know the start position

    def bfs(self, start, end):
        """perform a breadth first search from specified start node to end node"""
        q = [start]
        visited = set()
        parent = {}

        while q:
            s = q.pop(0)
            visited.add(s)
            acc = []
            for item in self.graph[s]:
                if item == end:
                    self._bfsPath = [item] + [s] + parent[s]
                    return True

                if item in visited:
                    continue

                if s in parent:
                    parent[item] = [s] + parent[s]
                else:
                    parent[item] = [s]

                acc += [item]

            q += acc

        return False

    def getBfsPath(self):
        """return bfs path from start node to end node of last bfs performed"""
        return "->".join([str(x) for x in self._bfsPath][::-1])

    def getBfsLen(self):
        """return bfs path length from start node to end node of last bfs performed"""
        return len(self._bfsPath) - 1

    def __str__(self):
        string_format = "{"
        for node in self.graph:
            string_format += f" {node} : ["
            for nodes in self.graph[node]:
                string_format += f"{nodes}, "
            string_format += "]; "
        string_format += "}"

        return string_format


if __name__ == '__main__':
    graph1 = Graph()
    graph1.addEdge(1, 2)
    graph1.addEdge(2, 3)
    graph1.addEdge(2, 1)
    graph1.addEdge(1, 4)
    graph1.addEdge(3, 5)
    graph1.addEdge(3, 6)
    print(graph1)
    print(graph1.dfs(1, 6))
    print(graph1.bfs(1, 6))
    print(graph1.getBfsPath(), graph1.getBfsLen())
