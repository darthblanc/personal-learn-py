# find out start and finish times for each vertex
def dfs(G, vertex, path, time):
    if vertex in path:
        return time
    path.add(vertex)
    phase1[vertex] = [time]
    for nbr in G[vertex]:
        time = dfs(G, nbr, path, time+1)
    phase1[vertex].append(time)
    return time+1

# transpose a graph, G
def transpose(G):
    g_t = {}
    for vertex in G:
        for nbr in G[vertex]:
            if nbr in g_t:
                g_t[nbr] |= {vertex}
            else:
                g_t[nbr] = {vertex}
    return g_t

# collect the components
def dfs_collect(G, vertex, seen, component):
    if vertex in seen:
        return
    seen.add(vertex)

    for nbr in G[vertex]:
        dfs_collect(G, nbr, seen, component)
    
    component.append(vertex)

# decomposition of transposed graph
def decompose(G):
    nbrs = [(phase1[node], node) for node in phase1]
    nbrs.sort(reverse=True)

    seen = set()
    components = []
    for nbr_details in nbrs:
        _, nbr = nbr_details
        if nbr not in seen:
            component = []
            dfs_collect(G, nbr, seen, component)
            components.append(component)
    return components
                    

if "__main__" == __name__:
    graph = {1:{3,4}, 2:{1}, 3:{2}, 4:{5}, 5:{}}
    parent_count = {}
    phase1 = {}
    dfs(graph, 1, set(), 1)
    graph_t = transpose(graph)
    components = decompose(graph)
    print(components)