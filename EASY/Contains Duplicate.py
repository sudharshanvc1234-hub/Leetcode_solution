# Date: 19-10-2026
# Problem Number: 217
# Problem Title: Contains Duplicate
# LeetCode Link: https://leetcode.com/problems/contains-duplicate/description/
# Difficulty: Easy
# Topic: Array, Brute Force
# Time Complexity: O(N**2)
# Space Complexity: O(1)
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False
        