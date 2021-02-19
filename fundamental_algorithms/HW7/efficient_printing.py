import math

# def print_neatly(l, n, m):
#  compute extras[i, j] for 1 <= i <= j <= n

    # for i <- 1 to n
        # do extras[i, j] <- M - 1_i
        # for j <- i + 1 to n
            # do extras[i, j] <- extras[i, j - 1] - 1_j - 1

# compute lc[i, j] for 1 <= i <= j <= n
    # for i <- 1 to n
        # do for j <- i to n
            # do if extras[i, j] < 0
                # then lc[i, j] <- ∞
            # else if j = n and extras[i, j] >= 0
                # then lc[i, j] <- 0
            # else lc[i, j] <- (extras[i, j])^3

# compute c[j] and p[j] for 1 <= j <= n

    # c[0] <- 0
    # for j <- 1 to n
        # do c[j] <- ∞
            # for i <- 1 to j
                # do if c[i - 1] + 1c[i, j] < c[j]
                    # then c[j] <- c[i - 1] + 1c[i, j]
                        # p[j] <- i
    # return c and p

# Here's how we print

# a

def extra_spaces(l, n, m):
    extras = []
    for i in range(1, n):
        extras[i, j] < - m - l[i]
    for j in range(i + 1, n):
        extras[i, j] = extras[i, j - 1] - l[j] - 1
    return extras

# b

def line_cost(extras, n):
    lc = []
    for i in range(1, n):
        for j in range(i, n):
            if extras[i, j] < 0:
                lc[i, j] = math.inf
            elif j == n and extras[i, j] >= 0:
                lc[i, j] = 0
            else:
                lc[i, j] = (extras[i, j])**3
    return lc

# c

def optimal_arrangement(lc, n):
    c = []
    c[0] = 0
    for j in range(1, n):
        c[j] = math.inf
        for i in range(1, j):
            if c[i - 1] + lc[i, j] < c[j]:
                c[j] = c[i - 1] + lc[i, j]
                p[j] = i
    return c, p


def print_lines(p, j):
    i = p[j]
    if i == 1:
        k = 1
    else:
        k = print_lines(p, i - 1) + 1
    return k

def print_paragraph(l, n, M):
    extras = compute_extras(l, n, m)
    lc = compute_line_cost(extras, n)
    c, p = compute_cost(lc, n)
    print_lines(p, n)


