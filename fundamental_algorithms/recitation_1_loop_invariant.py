import random

test_array = [1, 2, 3, 4, 5]


def sum_array(array):
    item_sum = 0
    for item in array:
        item_sum += item
    return item_sum


print(sum_array(test_array))

# reversing digits

n = int()
rev = 0
while n > 0:
    rev = rev * 10 + n % 10

jar_of_marbles = []

while len(jar_of_marbles) > 1:
    chosen_marbles = random.sample(jar_of_marbles, 2)
