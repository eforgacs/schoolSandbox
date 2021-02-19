from fundamental_algorithms.HW4.quicksort import partition


# looks like tail call optimized recursive quicksort

def quicksort_one_recursive_call(a, p, r):
    while p < r:
        q = partition(a, p, r)
        quicksort_one_recursive_call(a, p, q - 1)
        p = q + 1
    return a


def mod_quicksort(a, p, r):
    while p < r:
        q = partition(a, p, r)
        if q < (p + r) // 2:
            mod_quicksort(a, p, q - 1)
            p = q + 1
        else:
            mod_quicksort(a, q + 1, r)
            r = q - 1
    return a


test_array = [4, 3, 2, 1]

print(quicksort_one_recursive_call(test_array, 0, len(test_array) - 1))
