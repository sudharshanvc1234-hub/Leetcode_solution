# Date: 26-11-2026
# Problem Number: 1967
# Problem Title: Number of Strings That Appear as Substrings in Word
# LeetCode Link: https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/description/
# Difficulty: Easy
# Topic: Array, String
# Time Complexity: O(N*M*k)
# Space Complexity: O(1)


class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        count=0
        for i in patterns:
            if i in word:
                count +=1
        return count