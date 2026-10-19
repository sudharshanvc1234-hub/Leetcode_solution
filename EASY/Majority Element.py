# Date: 19-10-2026
# Problem Number: 169
# Problem Title: Majority Element
# LeetCode Link: https://leetcode.com/problems/majority-element/description/
# Difficulty: Easy
# Topic: Array, Conditional Statements
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None 
        count = 0 
        for num in nums: 
            if count == 0: 
                candidate = num 
            if num == candidate: 
                count += 1 
            else: count -= 1 
        return candidate