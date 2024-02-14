import heapq

if __name__ == "__main__":
    graph = {'A': [[2, 'B'], [3, 'C'], [3, 'D']], 'B': [[2, 'A'], [4, 'C'], [3, 'E']], 'C': [[3, 'A'], [5, 'D'], [6, 'F'], [1, 'E']], 'D': [[3, 'A'], [5, 'C'], [7, 'F']], 'E': [[8, 'F'], [1, 'C'], [3, 'B']], 'F': [[8, 'E'], [9, 'G']], 'G':[[9, 'F']]}

    for node in graph:
        heapq.heapify(graph[node])

    visited = {"A": 0}
    while len(visited) < len(graph):
        min_ = 2 ** 31
        cur  = ""
        itema = ""

        for item in visited:
            if not graph[item]:
                continue
            not_empty = True
            while graph[item][0][1] in visited:
                heapq.heappop(graph[item])
                if not graph[item]:
                    not_empty = False
                    break

            if not_empty:
                if graph[item][0][0] < min_:
                    min_ = graph[item][0][0]
                    cur = graph[item][0][1]
                    itema = item

        heapq.heappop(graph[itema])
        visited[cur] = min_
        heapq.heapify(graph[cur])
