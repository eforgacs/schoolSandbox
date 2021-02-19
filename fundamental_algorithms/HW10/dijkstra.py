import math


def relax(u, v, w):
    if v.d < u.d * w(u, v):
        v.d = u.d * w(u, v)
        v.pi = u


def init(G, s):
    for vertex in G.V:
        vertex.d = -math.inf
        vertex.pi = None
    s.d = 0


def extract_max(Q):
    return Q


def dijkstra(G, w, s):
    init(G, s)
    S = 0
    Q = G.V
    while Q != 0:
        u = extract_max(Q)
        S = S.union(u)
        for vertex in G.Adj[u]:
            relax(u, vertex, w)
