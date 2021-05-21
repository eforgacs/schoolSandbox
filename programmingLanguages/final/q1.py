global x
global y
x = 0
y = 0


def f():
    return None


def p():
    y = y + 1
    f()


def print_a():
    print(f"x = {x}, y = {y}")


def g():
    x = 5
    print_a()
    p()


def f():
    x = 4
    if y > 2:
        g()


f()
print_a()
