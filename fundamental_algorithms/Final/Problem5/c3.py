def topological_sort(a):
    return a.sort()


def longest_path(start, end):
    """✄ Input: Weighted DAG G = (V, E)
✄ Output: Largest path cost in G
Topologically sort G
for each vertex v ∈ V in linearized order
do dist(v) = max(u,v)∈E {dist(u) + w(u, v)}
return maxv∈V {dist(v)}
"""
    ordered_vertices = topological_sort(start)
    predecessors = get_predecessors(end)
    for vertex in ordered_vertices:
        dist[end] = max(dist)


def get_predecessors(v):
    pass


def longest_path_weights_and_edges(target, G):
    weights = {dictionary containing key, value pairs of edge: weight}
    vertices = G.topologically_sort()
    dist_weights = [0] * len(vertices)
    dist_paths = [None] * len(vertices)
    for v in vertices:
        # dist_weights.append(v.edge)
        for predecessor in get_predecessors(v):
            dist_v = dist_weights[predecessor] + weights[predecessor, v]
            if dist_v >= dist_weights[v]:
                # we have determined that dist_v is longest path at this point
                dist_paths[v] = dist_paths.get(predecessor)
                dist_paths[v].append(predecessor)
                dist_weights[v] = dist_v
        if v == target:
            return dist_paths[v].join(""), dist_weights[v]
            # dist_weights[v] = max(u,v) in E {dist(u) + w(u, v)}



def dist(vertex):
    return max(u, v) in E{dist(u) + 1}


