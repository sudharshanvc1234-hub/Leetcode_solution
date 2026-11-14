# Date: 14-11-2026
# Problem Number: 1351
# Problem Title: Count Negative Numbers in a Sorted Matrix
# LeetCode Link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/
# Difficulty: Easy
# Topic: 2D Array, Matrix
# Time Complexity: O(M * N)
# Space Complexity: O(1)


class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]<0:
                    count +=1
        return count