from math import floor, ceil

import numpy as np

n = 1
k = 1

decimal_array = np.linspace(0, 1, 11)
# A
for number in decimal_array:
    if not floor(floor(number / 2) / 2) == floor(number / 4):
        print(floor(floor(number / 2) / 2) == floor(number / 4))
        # print(floor(floor(x/2)/2) == floor(x/4))
# B
for k in range(1, 10_000):
    for n in range(1, 10_000):
        if not ceil(n / k) == floor((n - 1) / k) + 1:
            print("This is " + str((ceil(n / k) == floor((n - 1) / k) + 1)) + " when k = " + str(k) + " and n = " + str(
                n) + "\n")
