# Date: 27-11-2026
# Problem Number: 2000
# Problem Title: Reverse Prefix of Word
# LeetCode Link: https://leetcode.com/problems/reverse-prefix-of-word/
# Difficulty: Easy
# Topic: String
# Time Complexity: O(N)
# Space Complexity: O(N)


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                return word[:i+1][::-1] + word[i+1:]
        return word            