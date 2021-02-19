def nests(x, y, d):
    x = x.sort()
    y = y.sort()
    for i in range(len(d)):
        if x[i] >= y[i]:
            return False
    return True
