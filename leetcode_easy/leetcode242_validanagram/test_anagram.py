from unittest import TestCase
from leetcode_easy.leetcode242_validanagram.anagram import anagram


class AnagramTest(TestCase):

    def test_anagram_true(self):
        string_one = "Fried"
        string_two = "Fired"
        self.assertEqual(True, anagram(string_one, string_two))

    def test_anagram_false(self):
        string_one = "Fried"
        string_two = "Fires"
        self.assertEqual(False, anagram(string_one, string_two))

    def test_anagram_single_letter(self):
        string_one = "F"
        string_two = "F"
        self.assertEqual(True, anagram(string_one, string_two))

    def test_anagram_different_cases(self):
        string_one = "F"
        string_two = "f"
        self.assertEqual(True, anagram(string_one, string_two))

    def test_anagram_different_lengths(self):
        string_one = "John"
        string_two = "Johnson"
        self.assertEqual(False, anagram(string_one, string_two))
