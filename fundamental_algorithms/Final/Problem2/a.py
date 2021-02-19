# Python3 program to compute
# exponential value under
# modulo using binary
# exponentiation.

# prime modulo value
n = 1000000007


# Function code
def power(a, n):
    iterative_power_value = 1
    if n == 0:
        return 1
    elif n == 1:
        return a

    if n % 2 != 0:
        # return a ** (n-1) * a
        # the range function is exclusive on the upper bound, so it runs until n - 1
        for i in range(n):
            iterative_power_value = iterative_power_value * a
    else:
        # return (a ** 2) ** (n//2)
        square = a * a
        for i in range(n//2):
            iterative_power_value *= square
    return iterative_power_value


test_base = 2
test_exponent = 4

modulo = power(test_base, test_exponent)
print(modulo)
