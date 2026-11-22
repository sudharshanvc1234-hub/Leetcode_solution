# Date: 22-11-2026
# Problem Number: 2465
# Problem Title: Number of Distinct Averages
# LeetCode Link: https://leetcode.com/problems/number-of-distinct-averages/description/
# Difficulty: Easy
# Topic: Array, Two Pointers
# Time Complexity: O(N log N)
# Space Complexity: O(N)


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        averages = set()

        left = 0
        right = len(nums) - 1

        while left < right:
            avg = (nums[left] + nums[right]) / 2
            averages.add(avg)

            left += 1
            right -= 1

        return len(averages)