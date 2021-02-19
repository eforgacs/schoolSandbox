from unittest import TestCase

from Sandbox.fundamental_algorithms.Midterm.quicksort_one_recursive import quicksort_one_recursive_call, \
    mod_quicksort

ascending_array = [1, 2, 3, 4]
descending_array = [4, 3, 2, 1]

mixed_array = [2, 1, 4, 3, 6, 5, 8, 7]


class Test(TestCase):
    def test_quicksort_one_recursive_descending(self):
        self.assertEqual([1, 2, 3, 4], quicksort_one_recursive_call(descending_array, 0, len(descending_array) - 1))

    def test_quicksort_one_recursive_ascending(self):
        self.assertEqual([1, 2, 3, 4], quicksort_one_recursive_call(ascending_array, 0, len(ascending_array) - 1))

    def test_quicksort_one_recursive_mixed(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], quicksort_one_recursive_call(mixed_array, 0, len(mixed_array) - 1))

    def test_mod_quicksort_one_recursive_descending(self):
        self.assertEqual([1, 2, 3, 4], mod_quicksort(descending_array, 0, len(descending_array) - 1))

    def test_mod_quicksort_one_recursive_ascending(self):
        self.assertEqual([1, 2, 3, 4], mod_quicksort(ascending_array, 0, len(ascending_array) - 1))

    def test_mod_quicksort_one_recursive_mixed(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], mod_quicksort(mixed_array, 0, len(mixed_array) - 1))
