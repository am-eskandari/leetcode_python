"""
Nov 13 2022
Leetcode: easy

Two Sum - Leetcode 1 - HashMap - Python
https://www.youtube.com/watch?v=KLlXCFG5TnA
https://leetcode.com/problems/two-sum/
"""
"""

"""


def two_sum(nums: list, target: int) -> list:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers
    such that they add up to target.

    Each input would have exactly one solution, and same element will not be used twice.

    :param nums: list of integers
    :param target: integer
    :precondition: nums is a list of integers
    :precondition: target is an integer
    :postcondition: return indices of the two numbers such that they add up to target
    :return: list of indices

    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]

    >>> two_sum([3, 3], 6)
    [0, 1]
    """
    # create a dictionary to store the value and index of each element in nums
    # key: value of element in nums
    # value: index of element in nums
    nums_dict = {}

    # loop through nums
    for i in range(len(nums)):
        # if the target - nums[i] is in nums_dict
        if target - nums[i] in nums_dict:
            # return the index of target - nums[i] and the index of nums[i]
            return [nums_dict[target - nums[i]], i]
        # if the target - nums[i] is not in nums_dict
        else:
            # add nums[i] and its index to nums_dict
            nums_dict[nums[i]] = i

    # if no two numbers in nums add up to target, return empty list
    return []
