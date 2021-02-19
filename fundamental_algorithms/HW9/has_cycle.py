def has_cycle(g):
    for u in g.V:
        u.color = "white"
    seen = {}
    for u in g.V:
        if u.color == "white":
            return has_cycle_visit(g, seen, u)


def has_cycle_visit(g, seen, u):
    u.color = "gray"
    for v in g.adj[u]:
        if (u, v) not in seen:
            seen.add((u, v))
            seen.add((v, u))
            if v.color == "gray":
                return True
        if v.color == "white":
            if has_cycle_visit(g, seen, v):
                return True
    u.color = "black"
    return False
