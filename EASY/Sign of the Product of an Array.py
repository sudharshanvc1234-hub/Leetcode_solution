# Date: 23-11-2026
# Problem Number: 1822
# Problem Title: Sign of the Product of an Array
# LeetCode Link: https://leetcode.com/problems/sign-of-the-product-of-an-array/description/
# Difficulty: Easy
# Topic: Array, Math
# Time Complexity: O(N)
# Space Complexity: O(1)


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count = 0

        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                count += 1

        if count % 2 == 0:
            return 1
        else:
            return -1