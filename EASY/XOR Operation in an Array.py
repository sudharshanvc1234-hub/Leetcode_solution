# Date: 13-11-2026
# Problem Number: 1486
# Problem Title: XOR Operation in an Array
# LeetCode Link: https://leetcode.com/problems/xor-operation-in-an-array/description/
# Difficulty: Easy
# Topic: Maths , For loops
# Time Complexity: O(N)
# Space Complexity: O(1)


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0

        for i in range(n):
            result ^= start + 2 * i

        return result