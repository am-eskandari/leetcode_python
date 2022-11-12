"""
Nov 12 2022
Leetcode: easy
https://www.youtube.com/watch?v=9UtInBqnCgA
"""


def anagram(string_one, string_two):
    """
    Determine if two given strings are an leetcode242_validanagram; return True if they are an leetcode242_validanagram, else False.

    :param string_one: a string of a single word
    :param string_two: a string of a single word
    :precondition: string_one and string_two has to be a string containing single word
    :precondition: string_one and string_two has to be a string of the same length
    :postcondition: correctly determine if the strings are an leetcode242_validanagram
    :return: True if string_one and string_two are an leetcode242_validanagram, else False

    >>> test_string_one = "leetcode242_validanagram"
    >>> test_string_two = "nagaram"
    >>> leetcode242_validanagram(test_string_one, test_string_two)
    True

    >>> test_string_one = "rat"
    >>> test_string_two = "car"
    >>> leetcode242_validanagram(test_string_one, test_string_two)
    False
    """
    return sorted(list(string_one.lower())) == sorted(list(string_two.lower()))


def main():
    """
    Drive the program.
    """
    string_one = "Fried"
    string_two = "Fired"
    print(anagram(string_one, string_two))


if __name__ == '__main__':
    main()

