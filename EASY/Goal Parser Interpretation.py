# Date: 06-11-2026
# Problem Number: 1678
# Problem Title: Goal Parser Interpretation
# LeetCode Link: https://leetcode.com/problems/goal-parser-interpretation/description/
# Difficulty: Easy
# Topic: Conditional Statements, String
# Time Complexity: O(N)
# Space Complexity: O(N)


class Solution:
    def interpret(self, command: str) -> str:
        result=""
        for i in range(len(command)):
            if command[i] == "G":
                result += "G"
            elif command[i] == "(":
                if command[i+1] == ")":
                    result += "o"
                else:
                    result += "al"

        return result