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
        parent = {q[0]: {}}

        while q[0] != end:
            if visited.__contains__(q[0]):
                q.pop(0)
                continue
            visited.add(q[0])
            for edge in self.graph[q[0]]:
                if q.__contains__(edge):
                    continue
                q.append(edge)
                parent[edge] = {q[0]: parent[q[0]]}
            distance += 1
            q.pop(0)

        return True, distance // 2, self.write_path(parent[end], end)

    # work on this......
    def DFS(self, start, end, visited):
        if start in visited:
            print(f"Detected Cycle at {start}")
            return False

        if not (self.graph.__contains__(end) or self.graph.__contains__(start)):
            return False

        if start == end:
            return True

        rv = False
        for nodes in self.graph[start]:
            visited.add(start)
            rv = rv or self.DFS(nodes, end, visited | set(start))

        return rv

    def write_path(self, branch, end):
        path = f"{end} -> "

        while len(branch) != 0:
            for k in branch.keys():
                path += f"{k} -> "
                branch = branch[k]

        return path[:-4]

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
    my_graph = Graph()

    my_graph.addEdge("E", "Surname")
    my_graph.addEdge("Surname", "Surname")
    my_graph.addEdge("C", "Initial")
    my_graph.addEdge("Person", "F")
    # my_graph.addEdge("C", "Person")

    print(my_graph.DFS("E", "Initial", set()))
    # print(my_graph)

# Got nodes from Neelam Yadav on geeksforgeeks
# build a function to print the bfs path
# count the num of edges
# build a function to find dfs
# build function to check num parts of connected nodes/ unconnected
