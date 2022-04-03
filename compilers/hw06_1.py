x = 1


def f(a):
    return x + a


def g():
    x = 2
    f(0)


print(g())
