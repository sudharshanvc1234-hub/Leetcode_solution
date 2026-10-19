# Date: 19-10-2026
# Problem Number: 1
# Problem Title: Two Sum
# LeetCode Link: https://leetcode.com/problems/two-sum/description/
# Difficulty: Easy
# Topic: Array, Brute force
# Time Complexity: O(N**2)
# Space Complexity: O(1)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]