# Date: 19-10-2026
# Problem Number: 1
# Problem Title: Two Sum
# LeetCode Link: https://leetcode.com/problems/two-sum/description/
# Difficulty: Easy
# Topic: Array, Brute force
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            need = target - nums[i]

            if need in seen:
               return [seen[need], i] 
               
            seen[nums[i]] = i