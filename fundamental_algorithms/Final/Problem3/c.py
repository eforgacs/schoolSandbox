import random


def diff(li1, li2):
    return list(list(set(li1) - set(li2)) + list(set(li2) - set(li1)))


def has_memory(numbers_to_choose_from):
    """NO-MEMORY tries to guess each integer by naming an integer from
the range [1, n] uniformly at random.

Same as the previous problem, but we use the procedure HAS-MEMORY, which
remembers the previously seen integers. It then guesses by naming an integer uniformly
at random from those not yet seen."""
    answers = []
    seen = []
    for number in numbers_to_choose_from:
        guess = random.choice(diff(numbers_to_choose_from, seen))
        if guess == number:
            answers.append(True)
        else:
            answers.append(False)
        seen.append(number)
    return answers


list_of_input_numbers = [1, 2, 3, 4, 5]
random.shuffle(list_of_input_numbers)
print(has_memory(list_of_input_numbers))
