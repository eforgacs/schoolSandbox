from unittest import TestCase

from fundamental_algorithms.HW7 import get_probability


class Test(TestCase):
    def test_get_probability_one_die(self):
        self.assertAlmostEqual((1/6), get_probability([6], 1))

    def test_get_probability_two_dice(self):
        """Probability of rolling a 2 (two 1s) with 2 dice."""
        self.assertEqual((1/36), get_probability([6, 6], 2))

    def test_get_probability_three_dice(self):
        """Probability of rolling a 3 (three 1s) with 3 dice."""
        self.assertEqual((1/216), get_probability([6, 6, 6], 3))

    # def test_get_probability_three_dice_one_1(self):
    #     self.assertEqual((1/216), get_probability([6, 6, 6], 1))
