from unittest import TestCase

from fundamental_algorithms.Midterm.max_concurrency import max_concurrency

original_start_and_end_times = [[4, 7], [2, 5], [1, 3], [5, 8]]
zero_concurrent_start_and_end_times = []
one_concurrent_start_and_end_time = [[1, 2], [4, 5], [7, 8], [10, 11]]
two_concurrent_start_and_end_times = [[1, 2], [1, 5], [7, 8], [10, 11]]
three_concurrent_start_and_end_times = [[4, 7], [2, 5], [1, 3], [4, 8]]
four_concurrent_start_and_end_times = [[4, 7], [2, 5], [1, 5], [4, 8]]
five_concurrent_start_and_end_times = [[4, 7], [4, 7], [2, 5], [1, 5], [4, 8]]

start_and_end_times_same_end_different_beginning = [[1, 10], [2, 10], [3, 10], [4, 10]]
start_and_end_times_same_beginning_different_end = [[1, 10], [1, 11], [1, 12], [1, 13]]
start_and_end_times_same_beginning_different_end_2 = [[1, 10], [1, 9], [1, 8], [1, 7]]


class Test(TestCase):
    def test_max_concurrency_original(self):
        """This should be 2."""
        self.assertEqual(2, max_concurrency(original_start_and_end_times))

    def test_max_concurrency_zero(self):
        self.assertEqual(0, max_concurrency(zero_concurrent_start_and_end_times))

    def test_max_concurrency_one(self):
        self.assertEqual(1, max_concurrency(one_concurrent_start_and_end_time))

    def test_max_concurrency_two(self):
        self.assertEqual(2, max_concurrency(two_concurrent_start_and_end_times))

    def test_max_concurrency_three(self):
        self.assertEqual(3, max_concurrency(three_concurrent_start_and_end_times))

    def test_max_concurrency_four(self):
        self.assertEqual(4, max_concurrency(four_concurrent_start_and_end_times))

    def test_max_concurrency_five(self):
        self.assertEqual(5, max_concurrency(five_concurrent_start_and_end_times))

    def test_start_and_end_times_same_end_different_beginning(self):
        self.assertEqual(4, max_concurrency(start_and_end_times_same_end_different_beginning))

    def test_start_and_end_times_same_beginning_different_end(self):
        self.assertEqual(4, max_concurrency(start_and_end_times_same_beginning_different_end))

    def test_start_and_end_times_same_beginning_different_end_2(self):
        self.assertEqual(4, max_concurrency(start_and_end_times_same_beginning_different_end_2))
