# Reuse the idea of counting sort to solve the following problem: Given n integers in the
# range 0 to k, how many of them fall into range [a..b] for some a and b? Give two procedures:

# PREPROCESS(A, n, k) that accepts array A of n integers in the range 0 to k, spends
# Theta(n + k) time, and returns preprocessed input P.

# QUERY(P, a, b) that accepts preprocessed input P and two integers a and b, and answers
# how many of the original n integers fall into range [a..b] in Theta(1) time.


# For example
# in these 20 integers, how many integers fall between 7 - 11?
from typing import List

test_array = [14, 3, 5, 19, 7, 1, 2, 12, 13, 16, 4, 18, 6, 10, 9, 17, 20, 15, 8, 11]
test_duplicate_array = [14, 3, 5, 19, 7, 7, 7, 7, 1, 2, 12, 13, 16, 4, 18, 6, 10, 17, 20, 15, 8, 8, 8, 8, 8, 8, 8, 11]


def preprocess(a: List[int], n: int, k: int) -> List[int]:
    m = k + 1
    tally = [0] * m
    for i in range(0, n):
        tally[a[i]] += 1
    return tally


def query(p: List[int], a: int, b: int) -> int:
    count_sum = 0
    for i in range(a, b + 1):
        count_sum += p[i]
    return count_sum


preprocessed_array = preprocess(a=test_duplicate_array, n=len(test_duplicate_array), k=20)
print(query(p=preprocessed_array, a=7, b=11))
