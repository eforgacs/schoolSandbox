def match_with_gaps(T, P):
    n = len(T)
    m = len(P)
    match = [False] * n, [False] * m
    for j in range(1, m):
        if P[j] == "♢":
            match[i, j] = match[0, j - 1]
    for i in range(1, n):
        for j in range(1, m):
            if P[j] == "♢":
                match[i, j] = match[i, j - 1] or match[i - 1, j]
            elif P[j] == T[i]:
                match[i, j] = match[i - 1, j - 1]
            else:
                match[i, j] = False
    return match[n, m]
