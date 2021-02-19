def longest_path(start_node, end_node):
    """Longest paths in DAGs exhibit optimal substructure (you don’t need to prove
this), allowing us to decompose an optimal solution into smaller optimal solutions.

Let dist[v] be the length of a longest path from s to v. In the example above, dist[t] =
dist[c] + w(c, t). In turn, dist[c] is either dist[a] + w(a, c) or dist[b] + w(b, c).

Generalize this reasoning into a recursive definition for dist[v]."""

