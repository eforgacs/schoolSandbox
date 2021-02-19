s = 0
n = 7
for i in range(1, 2 ** n):
    for j in range(1, i):
        s = s + 1
print(f"s: {s}")
print(f"s / n = {s / n}")
print(f"s**(1/float(n)) = {s**(1/float(n))}")

print(f"2^(n+1) = {2 ** (n + 1)}")

#  2^(2n-n)-2^n
