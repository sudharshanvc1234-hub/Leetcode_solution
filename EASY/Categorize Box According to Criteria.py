# Date: 28-10-2026
# Problem Number: 2525
# Problem Title: Categorize Box According to Criteria
# LeetCode Link: https://leetcode.com/problems/categorize-box-according-to-criteria/description/
# Difficulty: Easy
# Topic: Conditional Statements
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume = length * width * height

        bulky = length >= 10**4 or width >= 10**4 or height >= 10**4 or volume >= 10**9
        heavy = mass >= 100

        if bulky and heavy:
            return "Both"
        elif bulky:
            return "Bulky"
        elif heavy:
            return "Heavy"
        else:
            return "Neither"