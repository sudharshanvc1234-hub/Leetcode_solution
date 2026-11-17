# Date: 17-11-2026
# Problem Number: 1773
# Problem Title: Count Items Matching a Rule
# LeetCode Link: https://leetcode.com/problems/count-items-matching-a-rule/description/
# Difficulty: Easy
# Topic: Array, String
# Time Complexity: O(N)
# Space Complexity: O(1)


class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0

        for i in range(len(items)):
            if ruleKey == "type" and items[i][0] == ruleValue:
                count += 1
            elif ruleKey == "color" and items[i][1] == ruleValue:
                count += 1
            elif ruleKey == "name" and items[i][2] == ruleValue:
                count += 1

        return count