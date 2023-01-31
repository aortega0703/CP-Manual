import math

def bellman_ford(V, E, source):
    D = [math.inf] * V
    D[source] = 0
    # |V| - 1 interations over all |E| edges
    for _ in range(V - 1):
        for w, u, v in E:
            # Update distance if improved using edge (u, v)
            if D[u] + w < D[v]:
                D[v] = D[u] + w
    
    # Extra |V|-th iteration
    for w, u, v in E:
        if D[u] + w < D[v]:
            # Negative weight cycle found
            return None
    return D