test_n = 1234


def get_digits(n):
    d = []
    # n // 10 ** (i - 1) % 10
    while n > 0:
        last_digit = n % 10
        d.append(last_digit)
        n = n // 10
    return d


print(get_digits(test_n))
