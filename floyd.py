# Floyd's algorithm for finding all-pairs shortest path
def floyd(graph):
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                through_k = graph[i][k] + graph[k][j]
                if through_k < graph[i][j]:
                    graph[i][j] = through_k
    return graph
