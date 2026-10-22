# Date: 22-10-2026
# Problem Number: 136
# Problem Title: Single Number
# LeetCode Link: https://leetcode.com/problems/single-number/
# Difficulty: Easy
# Topic: Array
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0

        for num in nums:
            result = result^num

        return result