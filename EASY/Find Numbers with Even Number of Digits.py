# Date: 23-10-2026
# Problem Number: 1295
# Problem Title: Find Numbers with Even Number of Digits
# LeetCode Link: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
# Difficulty: Easy
# Topic: Array, Maths
# Time Complexity: O(N * D)
# Space Complexity: O(D)
#D== maximum number of digits in any element.
class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0

        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1

        return count
