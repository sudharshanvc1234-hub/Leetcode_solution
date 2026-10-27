# Date: 27-10-2026
# Problem Number: 1365
# Problem Title: How Many Numbers Are Smaller Than the Current Number
# LeetCode Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
# Difficulty: Easy
# Topic: Array, For loos
# Time Complexity: O(N**2)
# Space Complexity: O(1)


class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        final = []

        for i in range(len(nums)):
            count = 0

            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1

            final.append(count)

        return final
