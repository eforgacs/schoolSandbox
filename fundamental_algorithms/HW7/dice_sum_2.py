# Python3 program to find the number of ways to get sum 'x' with 'n' dice
# where every dice has 'm' faces

def multiply_list(my_list):
    result = 1
    for x in my_list:
        result = result * x
    return result


def get_probability(D, k):
    total_ways = 0
    possible_outcomes = multiply_list(D)
    if k > len(D):
        return total_ways / possible_outcomes
    elif k == len(D):
        total_ways = k
    else:
        # cache = {}
        # for die in D:
            # if cache.get(die) is not None:
            #     total_ways += cache.get(die)
            # else:
        for die in D:
            for i in range(1, die):
                total_ways += find_ways_to_get_sum(m=die, n=len(D), x=k)
                # cache[die] = total_ways

    probability = total_ways / possible_outcomes
    return probability


# The main function that returns number of ways to get sum 'x'
# with 'n' dice and 'm' with m faces.
def find_ways_to_get_sum(m, n, x):
    # Create a table to store results of sub-problems. One extra
    # row and column are used for simplicity (Number of dice
    # is directly used as row index and sum is directly used
    # as column index). The entries in 0th row and 0th column
    # are never used.
    table = [[0] * (x + 1) for i in range(n + 1)]  # Initialize all entries as 0

    for j in range(1, min(m + 1, x + 1)):  # Table entries for only one dice
        table[1][j] = 1

    # Fill rest of the entries in table using recursive relation
    # i: number of dice, j: sum
    for i in range(2, n + 1):
        for j in range(1, x + 1):
            for k in range(1, min(m + 1, j)):
                table[i][j] += table[i - 1][j - k]

                # print(table)
    # Uncomment above line to see content of table

    return table[-1][-1]


# Driver code
D = [6, 6]
print(get_probability(D, 1))
# print(find_ways_to_get_sum(6, 2, 2))
# print(find_ways_to_get_sum(2, 2, 3))
# print(find_ways_to_get_sum(6, 3, 8))
# print(find_ways_to_get_sum(4, 2, 5))
# print(find_ways_to_get_sum(4, 3, 5))
