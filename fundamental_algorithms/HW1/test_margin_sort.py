from unittest import TestCase

from fundamental_algorithms.HW1 import margin_sort


class TestArrayData:
    test_array = [2, 1, 4, 3, 6, 5, 8, 7, 9]
    test_reverse_array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    test_sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    test_easy_array = [2, 1, 4, 3]
    test_odd_array = [3, 2, 1]
    test_single_element_array = [6]
    test_empty_array = []


class Test(TestCase):
    def test_margin_sort_basic_array(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], margin_sort(TestArrayData.test_array))

    def test_margin_sort_reverse_array(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], margin_sort(TestArrayData.test_reverse_array))

    def test_margin_sort_sorted_array(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], margin_sort(TestArrayData.test_sorted_array))

    def test_margin_sort_easy_array(self):
        self.assertEqual([1, 2, 3, 4], margin_sort(TestArrayData.test_easy_array))

    def test_margin_sort_odd_array(self):
        self.assertEqual([1, 2, 3], margin_sort(TestArrayData.test_odd_array))

    def test_margin_sort_single_element_array(self):
        self.assertEqual([6], margin_sort(TestArrayData.test_single_element_array))

    def test_margin_sort_empty_array(self):
        self.assertEqual([], margin_sort(TestArrayData.test_empty_array))
