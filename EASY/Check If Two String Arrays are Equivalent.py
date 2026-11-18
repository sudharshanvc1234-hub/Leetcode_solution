# Date: 18-11-2026
# Problem Number: 1662
# Problem Title: Check If Two String Arrays are Equivalent
# LeetCode Link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/
# Difficulty: Easy
# Topic: Array, String
# Time Complexity: O(N + M)
# Space Complexity: O(N + M)


class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        str1 = "".join(word1)
        str2 = "".join(word2)

        return str1 == str2