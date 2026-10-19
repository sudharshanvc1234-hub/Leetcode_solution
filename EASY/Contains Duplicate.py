# Date: 19-10-2026
# Problem Number: 217
# Problem Title: Contains Duplicate
# LeetCode Link: https://leetcode.com/problems/contains-duplicate/description/
# Difficulty: Easy
# Topic: Array, Brute Force
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set() 
        for num in nums: 
            if num in seen: 
                return True 
            seen.add(num) 
        return False
        
        