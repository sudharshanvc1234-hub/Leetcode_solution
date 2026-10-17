# Date: 17-10-2026
# Problem Number: 1342
# Problem Title: Number of Steps to Reduce a Number to Zero
# LeetCode Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
# Difficulty: Easy
# Topic: Loops,Conditional statements, String
# Time Complexity: O(logN)
# Space Complexity: O(1)

class Solution:
    def numberOfSteps(self, num: int) -> int:

        steps = 0

        while num > 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num - 1

            steps = steps + 1

        return steps