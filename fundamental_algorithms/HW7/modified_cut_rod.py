def modified_cut_rod(p, n, c):
    r = []
    r[0] = 0
    for j in range(1, n):
        q = p[j]
        for i in range(1, j - 1):
            q = max(q, p[i] + r[j - i] - c)
            r[j] = q
    return r[n]
