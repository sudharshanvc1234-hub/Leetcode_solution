# Date: 29-10-2026
# Problem Number: 2769
# Problem Title: Find the Maximum Achievable Number
# LeetCode Link: https://leetcode.com/problems/find-the-maximum-achievable-number/
# Difficulty: Easy
# Topic: Simple math
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num+2*t
        