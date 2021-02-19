# Python3 program to calculate 
# the probability of all the
# possible values that can
# be obtained throwing N dice

# def dice_probability(number_of_ones, sides):
#     # Initialize a 2d array upto
#     # (n*total sum possible) sum
#     # with value 0
#     dp = [[0 for j in range(1 * sides)]
#           for i in range(1 + 1)]
#
#     # Store the probability in a
#     # single throw for 1,2,3,4,5,6
#     for i in range(sides):
#         dp[1][i] = 1 / sides
#
#     # Compute the probabilities
#     # for all values from 2 to N
#     for i in range(2, 1 + 1):
#         for j in range(len(dp[i - 1])):
#             for k in range(sides):
#
#                 if (dp[i - 1][j] != 0 and
#                         dp[i - 1][k] != 0):
#                     dp[i][j + k] += (dp[i - 1][j] *
#                                      dp[1][k])
#
#                 # Print the result
#     # for i in range(len(dp[n]) - n + 1):
#     #     print(f"{i + n} {dp[n][i]:.3f}")
#     if 1 == number_of_ones:
#         return dp[1][0]
#     else:
#         return dp[1][1 - (number_of_ones * 1)]
#
#     # Driver code


# 1/6 * 1/20 * 1/8
# 0.0010416666666667


def multiply_list(my_list):
    result = 1
    for x in my_list:
        result = result * x
    return result


# def P(dice_array, number_of_ones):
#     table = []
#     # 1/2 * 2/3 + 1/2 * 1/3
#     # table = {
#     #     # 1: {0: a - 1 / a,
#     #     #     1: 1 / a}
#     # }
#     if not dice_array:
#         return 0
#     # if k is larger than the amount of dice
#     elif number_of_ones > len(dice_array):
#         return 0
#     #  e.g., [6, 6] 1/6 * 1/6 = 1/36
#     if number_of_ones == len(dice_array):
#         for die in dice_array:
#             table.append(1 / die)
#         return multiply_list(table)
#     else:
#         for die in dice_array:
#             for i in range(len(dice_array)):
#                 for j in range(i):
#                     print(dice_array[i][j])


def Q(dice_array, number_of_ones):
    single_combination_probability = 1
    for die in dice_array:
        single_combination_probability *= 1 / die
    num_paths = Q1(dice_array, number_of_ones, 0)
    return single_combination_probability * num_paths


def Q1(dice_array, usable_ones, current_die):
    memo = {}
    num_combinations = 0
    # traverse to next die or return or stop
    another_die = current_die < len(dice_array) - 1
    for die_value in range(1, dice_array[current_die] + 1):
        if another_die:
            if usable_ones > 0 and die_value == 1:
                # memoize the result of this recursive call into memo
                # if num_combinations in memo:
                #    pull result from memo
                # else:
                num_combinations += Q1(dice_array, usable_ones - 1, current_die + 1)
            else:
                # memoize the result of this recursive call into memo
                # if num_combinations in memo:
                #    pull result from memo
                # else:
                num_combinations += Q1(dice_array, usable_ones, current_die + 1)
        else:
            if usable_ones == 1 and die_value == 1:
                num_combinations += 1
            elif usable_ones == 0 and die_value != 1:
                num_combinations += 1
    return num_combinations


print(Q([6, 6, 6], 3))

# else:
#     for die in dice_array:
#         table.append(P(dice_array, number_of_ones - 1))


# print(dice_probability(number_of_ones=1, sides=6) *
#       dice_probability(number_of_ones=0, sides=6) *
#       dice_probability(number_of_ones=0, sides=6))
