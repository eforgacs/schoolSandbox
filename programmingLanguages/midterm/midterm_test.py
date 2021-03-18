def foo(x):
    for i in range(1, 10):
        print(f"x before: {x}")
        x = x + 1
        print(f"x after: {x}")


foo(1)
