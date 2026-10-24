# Date: 24-10-2026
# Problem Number: 2011
# Problem Title: Final Value of Variable After Performing Operations
# LeetCode Link: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
# Difficulty: Easy
# Topic: Array, String, Loops, Conditional Statements
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        X=0
        for operation in operations:
            if operation=="X++" or operation=="++X":
                X=X+1
            elif operation=="X--" or operation=="--X":
                X=X-1
        return X
