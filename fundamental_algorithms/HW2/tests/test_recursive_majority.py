from unittest import TestCase

from fundamental_algorithms.HW2.recursive_majority import recursive_majority

test_array = [1, 5, 3, 4, 2, 2, 5, 5, 5, 5]
binary_array = [1, 1, 2, 1, 2, 2, 1, 1]
left_heavy_array = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
right_heavy_array = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]


class Test(TestCase):
    def test_recursive_majority_test_array(self):
        self.assertEqual(5, recursive_majority(test_array))

    def test_recursive_majority_binary_array(self):
        self.assertEqual(1, recursive_majority(binary_array))

    def test_recursive_majority_left_heavy_array(self):
        self.assertEqual(1, recursive_majority(left_heavy_array))

    def test_recursive_majority_right_heavy_array(self):
        self.assertEqual(1, recursive_majority(right_heavy_array))
