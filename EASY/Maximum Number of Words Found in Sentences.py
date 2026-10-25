# Date: 25-10-2026
# Problem Number: 2114
# Problem Title: Maximum Number of Words Found in Sentences
# LeetCode Link: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/
# Difficulty: Easy
# Topic: Array, String
# Time Complexity: O(N * M)
# Space Complexity: O(M)

class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_count=0
        for sentence in sentences:
            count=len(sentence.split())
            if count>max_count:
                max_count=count
        return max_count