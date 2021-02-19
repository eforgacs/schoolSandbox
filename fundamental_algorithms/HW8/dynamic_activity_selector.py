# def dynamic_activity_selector(n):
# 	c[i,j] = 0
# 	for i in range(1, n):
# 		for j in range(2, n):
# 			if i >= j:
# 				c[i,j] = 0
#             else:
# 				for k in range(i+1, j-1):
# 					if c[i,j] < c[i,k] + c[k,j] + 1:
# 						c[i,j] = c[i,k] + c[k,j] + 1
# 							s[i,j] = k


def dynamic_activity_selector(s, f, n):
    c = []
    act = []
    for i in range(0, n):
        c[i, i] = 0
        c[i, i + 1] = 0
    c[n + 1, n + 1] = 0
    for l in range(2, n + 1):
        for i in range(0, n - l + 1):
            j = i + l
            c[i, j] = 0
            k = j - 1
            while f[i] < f[k]:
                if f[i] <= s[k] and f[k] <= s[j] and c[i, k] + c[k, j] + 1 > c[i, j]:
                    c[i, j] = c[i, k] + c[k, j] + 1
                    act[i, j] = k
                k = k - 1
    print(f"Set: {c[0, n + 1]}"
          f"Contents: {show_activities(c, act, 0, n + 1)}")


def show_activities(c, act, i, j):
    if c[i, j] > 0:
        k = act[i, k]
        print(k)
        show_activities(c, act, i, k)
        show_activities(c, act, k, j)


jobs = [
    (1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9),
    (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)
]

dynamic_activity_selector(jobs, 0, len(jobs))
