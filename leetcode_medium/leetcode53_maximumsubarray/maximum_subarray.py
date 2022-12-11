"""
Dec 10 2022
Leetcode: medium

Maximum Subarray - Amazon Coding Interview Question - Leetcode 53 - Python
https://www.youtube.com/watch?v=5WZl3MMT0Eg
https://leetcode.com/problems/two-sum/
"""


def maximum_subarray(nums: list) -> int:
    """
    Given an integer array nums, find the subarray which has the largest sum and return its sum.

    :param nums: a non-empty list of integers
    :precondition: nums must be a non-empty list of integers
    :postcondition: return the subarray which has the largest sum and return its sum
    :return: integer

    >>> maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    6

    >>> maximum_subarray([1])
    1

    >>> maximum_subarray([5, 4, -1, 7, 8])
    23
    """
    # create a variable to store the current sum
    current_sum = 0

    # create a variable to store the maximum sum
    maximum_sum = 0

    # loop through nums
    for i in range(len(nums)):
        # if the current sum is less than 0
        if current_sum < 0:
            # set the current sum to 0
            current_sum = 0

        # add nums[i] to the current sum
        current_sum += nums[i]

        # if the current sum is greater than the maximum sum
        if current_sum > maximum_sum:
            # set the maximum sum to the current sum
            maximum_sum = current_sum

    # return the maximum sum
    return maximum_sum
