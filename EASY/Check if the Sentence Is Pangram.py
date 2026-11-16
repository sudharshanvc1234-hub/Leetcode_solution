# Date: 16-11-2026
# Problem Number: 1832
# Problem Title: Check if the Sentence Is Pangram
# LeetCode Link: https://leetcode.com/problems/check-if-the-sentence-is-pangram/
# Difficulty: Easy
# Topic: Set , String
# Time Complexity: O(N)
# Space Complexity: O(1)


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        unique=set(sentence)
        if len(unique)==26:
            return True
        else:
            return False