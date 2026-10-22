# Date: 22-10-2026
# Problem Number: 268
# Problem Title: Missing Number
# LeetCode Link: https://leetcode.com/problems/missing-number/
# Difficulty: Easy
# Topic: Array, Maths
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums) 
        total = n * (n + 1) // 2 
        return total - sum(nums)