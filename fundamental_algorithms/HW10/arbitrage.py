def construct_graph(R):
    return R


def bellman_ford(G, w, s):
    pass


def print_path(G, u, pi):
    pass


def arbitrage_possible(R):
    G, w, s = construct_graph(R)
    if not bellman_ford(G, w, s):
        return True
    return False


def print_arbitrage(R):
    G, w, s = construct_graph(R)
    if bellman_ford(G, w, s):
        print("No arbitrage possible.")
        return
    for u, v in G.E:
        if v.d > u.d + w(u, v):
            print_path(G, u, u.pi)
            return
