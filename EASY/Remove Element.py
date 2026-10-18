# Date: 18-10-2026
# Problem Number: 27
# Problem Title: Remove Element
# LeetCode Link: https://leetcode.com/problems/remove-element/description/
# Difficulty: Easy
# Topic: Array, 2 Pointer
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k +=1
        return k
        