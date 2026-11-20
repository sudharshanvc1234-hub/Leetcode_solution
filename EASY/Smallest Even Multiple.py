# Date: 20-11-2026
# Problem Number: 2413
# Problem Title: Smallest Even Multiple
# LeetCode Link: https://leetcode.com/problems/smallest-even-multiple/description/
# Difficulty: Easy
# Topic: Math
# Time Complexity: O(1)
# Space Complexity: O(1)


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2==0:
            return n
        else:
            return 2*n
        