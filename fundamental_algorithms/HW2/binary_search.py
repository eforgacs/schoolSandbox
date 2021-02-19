def recursive_binary_search(array, low, high, number_to_find):
    if high >= low:

        middle = (high + low) // 2

        if array[middle] == number_to_find:
            return middle

        elif array[middle] > number_to_find:
            return recursive_binary_search(array, low, middle - 1, number_to_find)

        else:
            return recursive_binary_search(array, middle + 1, high, number_to_find)
    else:
        return None


test_array = [1, 2, 3, 4, 5]
x = 4
print(recursive_binary_search(test_array, 0, len(test_array) - 1, x))


def iterative_binary_search(array, number_to_find):
    low = 0
    high = len(array) - 1
    while low <= high:
        middle = (high + low) // 2
        if array[middle] < number_to_find:
            low = middle + 1
        elif array[middle] > number_to_find:
            high = middle - 1
        else:
            return middle
    return None


print(iterative_binary_search(test_array, x))
