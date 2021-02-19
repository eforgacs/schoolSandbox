import math

c = []
denom = []


def compute_change(n, d, k):
    for j in range(1, n):
        c[j] = math.inf
        for i in range(1, k):
            if j >= d[i] and 1 + c[j - d[i]] < c[j]:
                c[j] = 1 + c[j - d]
                denom[j] = d[i]
        return c and denom


def give_change(j, denom):
    if j > 0:
        give_change(j - denom[j], denom)
