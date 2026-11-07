# Date: 07-11-2026
# Problem Number: 202
# Problem Title: Happy Number
# LeetCode Link: https://leetcode.com/problems/happy-number/description/
# Difficulty: Easy
# Topic: Array, String
# Time Complexity: O(log N)
# Space Complexity: O(log N)

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            total = 0

            for digit in str(n):
                val = int(digit)
                total += val * val

            n = total

        return n == 1