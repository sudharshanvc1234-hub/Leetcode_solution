# Date: 19-11-2026
# Problem Number: 66
# Problem Title: Plus One
# LeetCode Link: https://leetcode.com/problems/plus-one/description/
# Difficulty: Easy
# Topic: Array
# Time Complexity: O(N)
# Space Complexity: O(N)


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = int("".join(map(str, digits)))        
        n = n + 1
        result = []
        
        for i in str(n):
            result.append(int(i))

        return result