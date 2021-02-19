test_array = [2, 1, 4, 3, 6, 5, 8, 7, 9]
test_reverse_array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
test_sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_easy_array = [2, 1, 4, 3]


def margin_sort(a):
    for i in range((len(a) + 1) // 2):  # iterate over 1/2 of length of the array+1: O(n/2) = O(n) (disregard constants)
        left_margin, right_margin = i, len(a) - i - 1
        middle = a[left_margin:right_margin + 1]
        min_val = max_val = middle[0]
        index_min, index_max = i, i
        for index, val in enumerate(middle[1:]):  # iterate over diminishing subset of array ( - 2 each loop): O(n/2) = O(n)
            if val < min_val:
                min_val = val
                index_min = index + i + 1
            else:
                if val > max_val:
                    max_val = val
                    index_max = index + i + 1
        a[left_margin], a[index_min] = a[index_min], a[left_margin]
        if i != index_max:
            a[right_margin], a[index_max] = a[index_max], a[right_margin]
    return a

# O(n) * O(n) = O(n^2)

# print(margin_sort(test_array))
# print(margin_sort(test_reverse_array))
# print(margin_sort(test_sorted_array))
print(margin_sort(test_easy_array))
