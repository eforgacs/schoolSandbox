def hash_delete(t, k):
    j = hash_search(t, k)
    if not j:
        return
    t[j] = 'deleted'


def hash_insert(t, k):
    i = 0
    while i != m:
        j = h(k, i)
        if t[j] is None or t[j] == 'deleted':
            t[j] = k
            return j
        else:
            i += 1


def hash_search(t, k):
    i = 0
    while t[j] is not None or i != m:
        j = h(k, i)
        if t[j] == k:
            return j
        i = i + 1
    return None
