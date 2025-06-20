"""
Nov 13 2022
Leetcode: easy

Two Sum - Leetcode 1 - HashMap - Python
https://www.youtube.com/watch?v=KLlXCFG5TnA
https://leetcode.com/problems/two-sum/
"""


def two_sum(nums: list, target: int):
    """
    Given an array of integers nums and an integer target, return indices of the two numbers
    such that they add up to target.

    Each input would have exactly one solution, and same element will not be used twice.

    :param nums: list of integers of minimum length 2
    :param target: integer
    :precondition: nums is a list of integers of minimum length 2
    :precondition: target is an integer
    :postcondition: return indices of the two numbers such that they add up to target
    :return: list of indices

    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]

    >>> two_sum([3, 3], 6)
    [0, 1]
    """
    # answer key
    # create a dictionary to store the value and index of each element in nums
    # key: value of element in nums
    # value: index of element in nums
    seen = {}

    # loop through nums
    for index, number in enumerate(nums):
        # if the target - nums[i] is in seen
        if target - number in seen.keys():
            # return the index of target - nums[i] and the index of nums[i]
            return [seen[target - nums[index]], index]
        # if the target - nums[i] is not in seen
        else:
            # add nums[i] and its index to seen
            seen[nums[index]] = index
    # if no two numbers in nums add up to target, return empty list
    return []


def main():
    print(two_sum([1, 2, 3], 5))


if __name__ == '__main__':
    main()
