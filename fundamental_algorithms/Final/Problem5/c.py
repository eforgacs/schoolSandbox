# https://www.geeksforgeeks.org/longest-path-in-a-directed-acyclic-graph-dynamic-programming/

# Python3 program to find the
# longest path in the DAG

# Function to traverse the DAG
# and apply Dynamic Programming
# to find the longest path
def dfs(node, adj, dp, vis):
    vis[node] = True
    for i in range(0, len(adj[node])):
        if not vis[adj[node][i]]:
            dfs(adj[node][i], adj, dp, vis)
        dp[node] = max(dp[node], 1 + dp[adj[node][i]])


def longest_path(adj, n):
    dp = [0] * (n + 1)
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, adj, dp, visited)
    ans = 0
    for i in range(1, n + 1):
        ans = max(ans, dp[i])
    return ans


def addEdge(adj, u, v):
    adj[u].append(v)


# Function that returns the longest path


# Driver Code
if __name__ == "__main__":
    n = 5
    adj = [[] for i in range(n + 1)]

    # Example-1
    addEdge(adj, 1, 2)
    addEdge(adj, 1, 3)
    addEdge(adj, 3, 2)
    addEdge(adj, 2, 4)
    addEdge(adj, 3, 4)

    print(longest_path(adj, n))
