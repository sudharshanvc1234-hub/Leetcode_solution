# Date: 11-11-2026
# Problem Number: 1523
# Problem Title: Count Odd Numbers in an Interval Range
# LeetCode Link: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/
# Difficulty: Easy
# Topic: Maths
# Time Complexity: O(1)
# Space Complexity: O(1)


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = (high + 1) // 2 - low // 2
        return count