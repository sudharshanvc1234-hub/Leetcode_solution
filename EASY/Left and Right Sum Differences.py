# Date: 03-11-2026
# Problem Number: 2574
# Problem Title: Left and Right Sum Differences
# LeetCode Link: https://leetcode.com/problems/left-and-right-sum-differences/description/
# Difficulty: Easy
# Topic: Array, For loops
# Time Complexity: O(N)
# Space Complexity: O(N)


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = []
        rightSum = []
        answer = []

        total = 0
        for i in range(len(nums)):
            leftSum.append(total)
            total += nums[i]

        total = 0
        rightSum = [0] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            rightSum[i] = total
            total += nums[i]

        for i in range(len(nums)):
            answer.append(abs(leftSum[i] - rightSum[i]))

        return answer
        