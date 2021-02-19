# def power(a, c):
#     d = 1
#     b = bin()
#     for i in range(len(b), 0, -1):
#         c = 2 * c
#         d = (d * d)
#         if b[i] == 1:
#             c = c + 1
#             d = (d * a)
#     return d
#
# base = 2
# exp = 2


def power(a, b, n):
    r = 1
    while 1:
        if b % 2 == 1:
            r = r * a % n
        b /= 2
        if b == 0:
            break
        a = a * a % n

    return r


base = 2
exp = 2

print(power(base, 10, exp))
