# Date: 21-10-2026
# Problem Number: 2894
# Problem Title: Divisible and Non-divisible Sums Difference
# LeetCode Link: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description/
# Difficulty: Easy
# Topic: Array, Conditional Statements
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1=[]
        num2=[]
        for i in range(1,n+1):
            if i % m != 0:
                num1.append(i)
            else:
                num2.append(i)
        return sum(num1)-sum(num2)