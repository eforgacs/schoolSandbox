import random


def no_memory(number, n):
    """n distinct integers 1, 2, . . . , n are shuffled and passed to the procedure NO-MEMORY one by one.
    NO-MEMORY tries to guess each integer by naming an integer from the range [1, n] uniformly at random.
    (As the name suggests, NO-MEMORY does not take into account what integers it has already seen.)
What is the expected number of times NO-MEMORY guesses correctly?
"""
    if random.randint(1, n) == number:
        return True
    else:
        return False


list_of_input_numbers = [1, 2, 3, 4, 5]
random.shuffle(list_of_input_numbers)
for number in list_of_input_numbers:
    print(no_memory(number, len(list_of_input_numbers)))
