def bellman(G: dict, src: str):
    distances = {vertex:float('inf') for vertex in G}
    distances[src] = 0
    
    for k in range(len(G)):
        for vertex in G:
            for neighbour in G[vertex]:
                if G[vertex][neighbour] + distances[vertex] < distances[neighbour]:
                    distances[neighbour] = G[vertex][neighbour] + distances[vertex]

    return distances

if __name__ == "__main__":
    graph = {
        '0': {'1': 2, '2': 6},
        '1': {'3': 5},
        '2': {'3': 8},
        '3': {'4': 10, '5': 15},
        '4': {'6': 2},
        '5': {'6': 6},
        '6': {}
    }

    for node in graph:
        for nbr in graph[node]:
            if node not in graph[nbr]:
                graph[nbr][node] = graph[node][nbr]
    print(bellman(graph, '0'))
