# Date: 26-10-2026
# Problem Number: 1512
# Problem Title: Number of Good Pairs
# LeetCode Link: https://leetcode.com/problems/number-of-good-pairs/
# Difficulty: Easy
# Topic: Array, For loop
# Time Complexity: O(N**2)
# Space Complexity: O(1)

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    count+=1
        return count