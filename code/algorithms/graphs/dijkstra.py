import math
import queue

def dijkstra(G, V, source):
    D = [math.inf] * V
    D[source] = 0
    q = queue.PriorityQueue()
    q.put((0, source))
    while not q.empty():
        w, u = q.get()
        # Checks if the entry is outdated
        if w > D[u]:
            continue
        for w, v in G[u]:
            # Update distance if improved using edge (u, v)
            if D[u] + w < D[v]:
                D[v] = D[u] + w
                q.put((D[v], v))
    return D