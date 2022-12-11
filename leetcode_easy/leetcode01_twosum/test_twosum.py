from unittest import TestCase
from leetcode_easy.leetcode01_twosum.twosum import two_sum


class TwosSumTest(TestCase):

    def test_two_sum(self):
        self.assertEqual([1, 2], two_sum([1, 2, 3], 5))

    def test_two_sum_list_size_two(self):
        self.assertEqual([0, 1], two_sum([0, 1], 1))

    def test_two_sum_negative(self):
        self.assertEqual([1, 2], two_sum([-1, -2, -3], -5))

    def test_two_sum_empty(self):
        self.assertEqual([], two_sum([], 5))

    def test_two_sum_target_DNE(self):
        self.assertEqual([], two_sum([2, 6], 5))
