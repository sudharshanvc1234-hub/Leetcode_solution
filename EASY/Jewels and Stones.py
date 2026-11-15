# Date: 15-11-2026
# Problem Number: 771
# Problem Title: Jewels and Stones
# LeetCode Link: https://leetcode.com/problems/jewels-and-stones/description/
# Difficulty: Easy
# Topic: String
# Time Complexity: O(N * M)
# Space Complexity: O(1)


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        for ch in stones:
            if ch in jewels:
                count += 1
        return count