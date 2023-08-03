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

    def __str__(self):
        string_format = "{"
        for node in self.graph:
            string_format += f" {node} : ["
            for nodes in self.graph[node]:
                string_format += f"{nodes}, "
            string_format += "]; "
        string_format += "}"

        return string_format
