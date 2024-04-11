a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

n = len(a)

a[0] = a[0] * b[n - 1]  # run using thread 1
a[1] = a[1] * b[n - 2]  # run using thread 2
a[2] = a[2] * b[n - 3]  # run using thread 3...
a[3] = a[3] * b[n - 4]

print(a)
