# Date: 10-11-2026
# Problem Number: 2148
# Problem Title: Count Elements With Strictly Smaller and Greater Elements 
# LeetCode Link: https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/description/
# Difficulty: Easy
# Topic: Array, Sorting
# Time Complexity: O(N)
# Space Complexity: O(1)


class Solution:
    def countElements(self, nums: list[int]) -> int:
        return sum(1 for x in nums if min(nums)<x<max(nums))