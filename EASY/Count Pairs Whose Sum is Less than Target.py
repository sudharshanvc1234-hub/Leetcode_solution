# Date: 02-11-2026
# Problem Number: 2824
# Problem Title: Count Pairs Whose Sum is Less than Target
# LeetCode Link: https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/
# Difficulty: Easy
# Topic: Array, Two Pointers, Sorting
# Time Complexity: O(N log N)
# Space Complexity: O(1)

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1
        count = 0

        while left < right:
            if nums[left] + nums[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1

        return count