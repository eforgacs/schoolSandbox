def power(a, n):
    d = 1
    while n > 0:
        if n % 2 == 1:
            d = d * a
        n = n / 2
        if n > 0:
            a = a * a
    return d

print(power(2, 2))
