# Leetcode 11: Container with Most Water - https://leetcode.com/problems/container-with-most-water/description/
# April 20th, 2025

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # area = min(height[left], height[right]) * (right - left)
            # lists_area.append(area)

            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# Example usage for local testing
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    heights1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(solution.maxArea(heights1))  # Expected: 49

    heights2 = [1, 1]
    print(solution.maxArea(heights2))  # Expected: 1

    heights3 = [8,7,2,1]
    print(solution.maxArea(heights3))  # Expected: 7
