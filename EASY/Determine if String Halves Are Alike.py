# Date: 08-11-2026
# Problem Number: 1704
# Problem Title: Determine if String Halves Are Alike
# LeetCode Link: https://leetcode.com/problems/determine-if-string-halves-are-alike/
# Difficulty: Easy
# Topic: Conditional Statements , String
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count = 0
        n = len(s)

        for i in range(n//2):
            if s[i] in "aeiouAEIOU":
                count += 1

            if s[i+n//2] in "aeiouAEIOU":
                count -= 1

        return count == 0