# Date: 21-11-2026
# Problem Number: 1952
# Problem Title: Three Divisors
# LeetCode Link: https://leetcode.com/problems/three-divisors/description/
# Difficulty: Easy
# Topic: Math
# Time Complexity: O(N)
# Space Complexity: O(1)


class Solution:
    def isThree(self, n: int) -> bool:
        count = 0

        for i in range(1, n+1):
            if n % i == 0:
                count += 1

        return count == 3