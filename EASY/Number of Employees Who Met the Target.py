# Date: 01-11-2026
# Problem Number: 2798
# Problem Title: Number of Employees Who Met the Target
# LeetCode Link: https://leetcode.com/problems/number-of-employees-who-met-the-target/description/
# Difficulty: Easy
# Topic: Array, For loops
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count=0
        for i in range(0,len(hours)):
            if hours[i]>=target:
                count+=1
        return count       