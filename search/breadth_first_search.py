class Graph:

    # Constructor
    def __init__(self):
        self.graph = {}

    # Function to add an edge to graph
    def addEdge(self, node1, node2):
        if node1 == node2:
            self.graph[node1].append(node1)
        if not self.graph.__contains__(node1):
            self.graph[node1] = []
        if not self.graph.__contains__(node2):
            self.graph[node2] = []
        if not self.graph[node1].__contains__(node2):
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)

    def add(self, node):
        if not self.graph.__contains__(node):
            self.graph[node] = []

    def numVertices(self):
        return len(self.graph)

    # Function to print a BFS of graph
    def BFS(self, start, end):
        if not (self.graph.__contains__(end) or self.graph.__contains__(start)):
            return False

        distance = 1
        q = [start]
        visited = set()
        while q[0] != end:
            if visited.__contains__(q[0]):
                q.pop(0)
                continue
            visited.add(q[0])
            for edge in self.graph[q[0]]:
                q.append(edge)
            distance += 1
            q.pop(0)
        return True, distance

    def __str__(self):
        string_format = "{"
        for node in self.graph:
            string_format += f" {node} : ["
            for nodes in self.graph[node]:
                string_format += f"{nodes}, "
            string_format += "]; "
        string_format += "}"

        return string_format


# Driver code
if __name__ == '__main__':
    # Create a graph given in
    # the above diagram
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.addEdge(2, 5)
    g.addEdge(3, 7)
    print(g.numVertices())
    # print(g.numEdges())
    print(g)
    found, distance = g.BFS(1, 3)
    print(found, distance // 2)

# This code is contributed by Neelam Yadav
# build a function to print the bfs path
# count the num of edges
# build a function to find dfs
# build function to check num parts of connected nodes/ unconnected
