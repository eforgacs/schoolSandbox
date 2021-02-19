def longest_path_weight(G(E, V)):
    add s and t
    negate edge weights
    G.topological_sort()
    for u in sorted_vertices:
        for v in G.adj[u]:
            relax(u, v)

def relax(u, v):
	if dist[v] > dist[u] + w(u, v):
		dist[v] = dist[u] + w(u, v)
		parents[v] = u
    elif dist[v] == dist[u] + w(u, v):
		parents.[v].append(u)
