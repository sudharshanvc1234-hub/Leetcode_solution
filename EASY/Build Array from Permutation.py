# Date: 24-10-2026
# Problem Number: 1920
# Problem Title: Build Array from Permutation
# LeetCode Link: https://leetcode.com/problems/build-array-from-permutation/
# Difficulty: Easy
# Topic: Array, String
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans=[]
        for i in range(0,len(nums)):
            ans.append(nums[nums[i]])
        return ans