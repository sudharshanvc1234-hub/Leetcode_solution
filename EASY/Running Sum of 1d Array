# Date: 16-10-2026
# Problem Number: 1480
# Problem Title: Running Sum of 1d Array
# LeetCode Link: https://leetcode.com/problems/running-sum-of-1d-array/
# Difficulty: Easy
# Topic: Array
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        return nums