# Date: 31-10-2026
# Problem Number: 2652
# Problem Title: Sum Multiples
# LeetCode Link: https://leetcode.com/problems/sum-multiples/description/
# Difficulty: Easy
# Topic: Maths
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sum=0
        for i in range(0,n+1):
            if i%3==0 or i%5==0 or i%7==0:
                sum+=i
        return sum