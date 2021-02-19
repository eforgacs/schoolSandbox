m = 10

keys = [857, 745, 525, 286, 856, 125, 659, 435, 514]


def hash_function(k, i):
    return ((k % m) + i) % m


for key in keys:
    for i in range(m - 1):
        print(f"{key}: {i} = {hash_function(key, i)}")
