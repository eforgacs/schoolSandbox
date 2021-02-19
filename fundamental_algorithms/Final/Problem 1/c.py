def divide_and_conquer(array):
    """A procedure accepts an array, splits it in two equal halves in constant time, performs a quadratic amount of work
     on each half, then calls itself recursively on only one of the halves.
    The running time of this procedure is quadratic."""
    if not array:
        return 0
    work = len(array) ** 2
    lower_half = array[:len(array) // 2]
    return work + divide_and_conquer(lower_half)


m = 5
# n = 2^5 = 32, work, 1024 + 256 + 64 + 16 + 4 + 1
# n = 2^4 = 16, work,        256 + 64 + 16 + 4 + 1
# n = 2^3 = 8, work,               64 + 16 + 4 + 1
# n = 2^2 = 4, work,                    16 + 4 + 1
# n = 2^1 = 2, work,                    16 + 4 + 1
n = 2 ** m
test_array = [0] * n
print(divide_and_conquer(test_array))
