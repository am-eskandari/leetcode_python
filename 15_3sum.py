# Leetcode 15: 3-Sum - https://leetcode.com/problems/3sum/description/
# April 26th, 2025

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)

        # result = []
        result = set()

        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1

            while left < right:
                sums = nums[i] + nums[left] + nums[right]

                if (sums) < 0:
                    left = left + 1
                if (sums) > 0:
                    right = right - 1
                if (sums) == 0:
                    # result.append([nums[i], nums[left], nums[right]])
                    result.add((nums[i], nums[left], nums[right]))
                    break

                # triplet = tuple(sorted([nums[i], nums[left], nums[right]]))
                # triplets.add(triplet)

        return [list(triplet) for triplet in result]

        # if (sums) > 0:
        #     sums = nums[left] + nums[right] + nums[left + 1]
        #     if (sums) == 0:
        #         result.append([nums[left], nums[right], nums[left + 1]])
        #
        # if (sums) < 0:
        #     sums = nums[left] + nums[right] + nums[right - 1]
        #     if (sums) == 0:
        #         result.append([nums[left], nums[right], nums[right - 1]])
        #
        # if (sums) == 0:
        #     if (nums[left + 1] == 0):
        #         sums = nums[left] + nums[right] + nums[left + 1]
        #     if (nums[right - 1] == 0):
        #         sums = nums[left] + nums[right] + nums[right - 1]

        # return result


if __name__ == "__main__":
    solution = Solution()

    # Test cases

    nums00 = [-2, 0, 1, 1, 2]
    print(solution.threeSum(nums00))  # Expected:

    nums01 = [0, 0, 0, 0]
    print(solution.threeSum(nums01))  # Expected:

    nunms = [-1, 0, 1, 2, -1, -4]
    print(solution.threeSum(nunms))  # Expected:

    nums2 = [0, 1, 1]
    print(solution.threeSum(nums2))  # Expected:

    nums3 = [0, 0, 0]
    print(solution.threeSum(nums3))  # Expected:
