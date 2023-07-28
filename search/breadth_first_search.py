# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.

from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):
        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def addEdge(self, node1, node2):
        self.graph[node1].append(node2)

    # Function to print a BFS of graph
    def BFS(self, start, end):
        if not (self.graph.__contains__(end) or self.graph.__contains__(start)):
            return False

        q = [start]
        visited = set()
        while q[0] != end:
            if visited.__contains__(q[0]):
                q.pop(0)
                continue
            visited.add(q[0])
            for edge in self.graph[q[0]]:
                q.append(edge)
            q.pop(0)

        return True


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
    # print(g)
    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    print(g.BFS(1, 3))

# This code is contributed by Neelam Yadav
