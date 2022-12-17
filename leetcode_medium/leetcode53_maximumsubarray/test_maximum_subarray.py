from unittest import TestCase
from leetcode_medium.leetcode53_maximumsubarray.maximum_subarray import maximum_subarray


class MaxSubarrayTest(TestCase):
    def test_maximum_subarray(self):
        actual = maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        expected = 6
        self.assertEqual(expected, actual)

    def test_maximum_subarray_size_one(self):
        actual = maximum_subarray([2])
        expected = 2
        self.assertEqual(expected, actual)