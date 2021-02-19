def counting_sort(B, max_val):
    m = max_val + 1
    C = [0] * m

    for a in B:
        # count occurrences
        C[a] += 1
    i = 0
    for a in range(m):
        for c in range(C[a]):
            B[i] = a
            i += 1
    return B


A = [4, 6, 3, 5, 0, 5, 1, 3, 5, 5]
print(counting_sort(A, max(A)))
