from unittest import TestCase

from fundamental_algorithms.HW3.preprocess import preprocess, query

test_array = [14, 3, 5, 19, 7, 1, 2, 12, 13, 16, 4, 18, 6, 10, 9, 17, 20, 15, 8, 11]
test_duplicate_array = [14, 3, 5, 19, 7, 7, 7, 7, 1, 2, 12, 13, 16, 4, 18, 6, 10, 17, 20, 15, 8, 8, 8, 8, 8, 8, 8, 11]


class Test(TestCase):
    def test_query_array(self):
        preprocessed_array = preprocess(a=test_array, n=len(test_array), k=20)
        self.assertEqual(5, query(p=preprocessed_array, a=7, b=11))

    def test_query_duplicate_array(self):
        preprocessed_array = preprocess(a=test_duplicate_array, n=len(test_duplicate_array), k=20)
        self.assertEqual(13, query(p=preprocessed_array, a=7, b=11))
