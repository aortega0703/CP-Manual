# Receives the Graph G and it's transpose G2
def kosaraju(G, G2, V):    
    # Uses C to store both components and visited status
    def DFS(G, u, c = True):
        stack = [u]
        C[u] = c
        while stack:
            u = stack[-1]
            for v in G[u]:
                if C[v] is None:
                    C[v] = c
                    stack.append(v)
                    break
            else:
                post.append(u)
                stack.pop()
    # Fills post numbers on first DFS pass
    C = [None] * V
    post = []
    for u in range(V):
        if C[u] is None:
            DFS(G, u)
    # Traverses G2 on post order and fills components
    C = [None] * V
    c = 0
    while post:
        u = post.pop()
        if C[u] is None:
            DFS(G2, u, c)
            c += 1
    return C, c