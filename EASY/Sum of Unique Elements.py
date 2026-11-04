# Date: 04-11-2026
# Problem Number: 1748
# Problem Title: Sum of Unique Elements
# LeetCode Link: https://leetcode.com/problems/sum-of-unique-elements/
# Difficulty: Easy
# Topic: Array ,Hash table 
# Time Complexity: O(N)
# Space Complexity: O(N)


class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1

        total = 0

        for i in count:
            if count[i] == 1:
                total += i

        return total