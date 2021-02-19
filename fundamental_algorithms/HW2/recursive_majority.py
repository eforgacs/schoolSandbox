# In an n-element array, the majority element is the one that repeats more
# than n/2 times. Assume that the majority element is always present in the array.
# Consider the following mergesort-like approach to finding the majority element: split A in two
# halves; recursively find "local" majority elements in each half; combine the solutions.
# Give a subquadratic-time procedure RECURSIVE-MAJORITY(A) that implements this idea. Formulate
# and solve the recurrence describing the worst-case running time.


"""

RECURSIVE-MAJORITY(A):
    given an array of n elements, there is a value v that occurs more than n/2 times.
    e.g. most basic case; [2]
    
    get the midpoint of the array
    use the midpoint to split the array into left and right arrays
    
    recursively call RECURSIVE-MAJORITY on left and right arrays
    
    find the majority element in A
    record the majority element so far in global variable
    
"""
test_array = [1, 5, 3, 4, 2, 2, 5, 5, 5, 5]
binary_array = [1, 1, 2, 1, 2, 2, 1, 1]
left_heavy_array = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
right_heavy_array = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]


def recursive_majority_finder(array):
    """Unfinished."""
    # Given an array containing n elements, with a majority x where x > n/2,
    # bisecting the array will generate at least one array of m elements with the majority of those n elements
    if len(array) == 1:
        return array[0]
    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]
    left_majority = recursive_majority_finder(left_array)
    right_majority = recursive_majority_finder(right_array)

    if left_majority is None:
        return right_majority
    elif right_majority is None:
        return left_majority
    elif left_majority == right_majority:
        return left_majority
    else:
        return None


# def recursive_majority(a):
#     def recursive_majority_executor(low, high):
#         if low == high:
#             return a[low]
#
#         mid = (high - low) // 2 + low
#         left = recursive_majority_executor(low, mid)
#         right = recursive_majority_executor(mid + 1, high)
#
#         if left == right:
#             return left
#
#         left_count = 0
#         for i in range(low, high + 1):
#             if a[i] == left:
#                 left_count += 1
#
#         right_count = 0
#         for i in range(low, high + 1):
#             if a[i] == right:
#                 right_count += 1
#
#         return left if left_count > right_count else right
#
#     return recursive_majority_executor(0, len(a) - 1)


def recursive_majority(a):
    # given an array with a majoritive element x
    # bisecting the array will provide at least 1 subarray with a majoritive element x

    # stopping case
    if len(a) == 1:
        return a[0]

    mid = len(a) // 2
    left_subarray = a[:mid]
    right_subarray = a[mid:]

    # special case need to resolve majority of len 3 array
    # due to incongruity
    if len(right_subarray) == 3:
        if right_subarray[0] == right_subarray[1] or \
                right_subarray[0] == right_subarray[2]:
            right_majority = right_subarray[0]
        elif right_subarray[1] == right_subarray[2]:
            right_majority = right_subarray[1]
        else:
            right_majority = None
    else:
        right_majority = recursive_majority(right_subarray)
    left_majority = recursive_majority(left_subarray)

    if left_majority is not None and right_majority is not None:
        if left_majority != right_majority:
            return None
        return left_majority
    elif left_majority is None:
        return right_majority
    else:
        return left_majority


print(recursive_majority(test_array))
